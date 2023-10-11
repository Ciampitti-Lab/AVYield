from pymongo.mongo_client import MongoClient
from config import sv_config, config
import pandas as pd
from bson.json_util import dumps, loads


client = MongoClient(sv_config.mongodb_uri)


# ========== Data Page Queries==========#
# Get Dropdowns
def get_data_dict(dataset_name, first_selection=None):
    db = client['kansas-crop-trials']
    collection = db[dataset_name]

    if first_selection is None:
        pipeline = [
            {"$group": {"_id": "$YEAR"}},
            {"$sort": {"_id": 1}}
        ]
        unique_values = list(collection.aggregate(pipeline))
        formatted_values = [
            {
                'label': str(value["_id"]),
                'value': value["_id"]} for value in unique_values
        ]
        return formatted_values, formatted_values[0]['value']
    else:
        pipeline = [
            {"$group": {"_id": "$YEAR"}},
            {"$match": {"_id": {"$gte": first_selection}}},
            {"$sort": {"_id": 1}}
        ]
        available_years = list(collection.aggregate(pipeline))

        # Extract the filtered years and the end year
        filtered_years = [year["_id"] for year in available_years]
        end_year_value = filtered_years[-1] if filtered_years else None

        # Format the result as a list of dictionaries
        formatted_years = [{'label': str(year), 'value': year}
                           for year in filtered_years]

        return formatted_years, end_year_value


def get_data(dataset_name, start_year, end_year):
    db = client['kansas-crop-trials']
    filter_query = {
        "YEAR": {"$gte": start_year, "$lte": end_year}
    }
    return pd.DataFrame(list(db[dataset_name].find(filter_query, {"_id": 0})))


# ========== Compare Page Queries==========#
# Get Dropdown dict
def get_compare_dict(dataset_name, filter_field, first_selection=None):
    db = client['kansas-crop-trials']
    collection = db[dataset_name]

    if first_selection is None:
        pipeline = [
            {"$group": {"_id": f"${'YEAR' if filter_field == 'genotype' else 'NAME'}"}},
            {"$sort": {"_id": 1}}
        ]
    else:
        if filter_field == 'genotype':
            pipeline = [
                {"$match": {"YEAR": first_selection}},
                {"$group": {"_id": "$NAME"}},
                {"$sort": {"_id": 1}}
            ]
        else:
            pipeline = [
                {"$match": {"NAME": first_selection}},
                {"$group": {"_id": "$YEAR"}},
                {"$sort": {"_id": 1}}
            ]

    unique_values = list(collection.aggregate(pipeline))
    formatted_values = [
        {'label': str(value["_id"]), 'value': value["_id"]} for value in unique_values
    ]
    return formatted_values, formatted_values[-1]['value']


#
def get_compare_yield_bar_df(dataset_name, filter, first_opt, second_opt, conv_rate):
    db = client['kansas-crop-trials']
    collection = db[dataset_name]

    col1, col2 = ('YEAR', 'NAME') if filter == 'genotype' else ('NAME', 'YEAR')
    # Match documents for the selected crop and convert the YEAR field to a string
    
    pipeline = [
        {"$addFields": {"YEAR": {"$toString": "$YEAR"}}},
        {"$match": {col1: first_opt}},
        {"$match": {col2: {"$in": second_opt}}},
        {"$group": {"_id": {"$concat": ["$WATER_REGIME", col2]}, "YIELD": {"$avg": "$YIELD"}}},
        {"$project": {"WATER_REGIME": "$_id", "YIELD": 1, "_id": 0}},
        {"$addFields": {"YIELD": {"$multiply": ["$YIELD", conv_rate]}}},
        {"$addFields": {"YIELD": {"$round": ["$YIELD", 2]}}}
    ]


    # Execute the aggregation pipeline
    result = list(collection.aggregate(pipeline))

    # Convert the result to a Pandas DataFrame if needed
    df = pd.DataFrame(result)

    return df

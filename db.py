from box import Box
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

sv_config = Box.from_yaml(filename=".env/sv_config.yml")
client = MongoClient(sv_config.mongodb_uri)


# ========== Env Queries==========#
def get_config(ff, sf=None):
    res = client['environment']['config'].find_one({}, {'_id': 0})
    return res[ff] if sf is None else res[ff][sf]


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


# Get df for visualizations
def get_compare_df(dataset_name, filter, first_opt, second_opt, conv_rate):
    db = client['kansas-crop-trials']
    collection = db[dataset_name]

    col1, col2 = ('YEAR', 'NAME') if filter == 'genotype' else ('NAME', 'YEAR')

    pipeline = [
        {"$addFields": {"YEAR": {"$toString": "$YEAR"}}},
        {"$match": {col1: first_opt}},
        {"$match": {col2: {"$in": second_opt}}},
        {"$addFields": {"YIELD": {"$multiply": ["$YIELD", conv_rate]}}},
        {"$addFields": {"YIELD": {"$round": ["$YIELD", 2]}}}
    ]

    return pd.DataFrame(list(collection.aggregate(pipeline))), col2


# Get geodata
def get_geodata():
    db = client['geodata']
    collection = db['kansas-counties']

    features = list(collection.find({}, projection={'_id': 0}))
    feature_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    return json.dumps(feature_collection)

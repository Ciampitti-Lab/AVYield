import pandas as pd
from thefuzz import process

"""
Conclusions:
    Canola: !! done !!
        -- No way of knowing.
    Corn: !! done !!
        --NAME: both cases could be fixed by using upper(NAME)
        --BRAND: casing issues
    Sorghum: !! done !!
        --NAME: both cases could be fixed by using upper(NAME)
        --BRAND: casing issues
    Soybean:
        --NAME: pretty confident that they aren't typos, should leave it be. 
        --BRAND: casing issues
    Sunflower: !! done !!
        --NAME: equal pcdoes with diff names could be fixed by using upper(NAME)
        --BRAND: casing issues
    Wheat: !! done !!
        --NAME: equal names with diff pcodes could be fixed by using upper(NAME)
        --BRAND: casing issues

Course of Action:
    NAME: !!done!!
        i-Force unique_entry to uppercase.
        ii-Match the names with same pcode.
        iii-Match the names with diff pcode with Soybean as an exception.
        
    BRAND: !!done!!
        Force uppercase in all entries.
"""


def col_to_upper(df, col):
    df[col] = df[col].str.upper()
    return df


def coa_name_two(df):
    unique_entries = df["NAME"].fillna(0).unique()
    unique_entries = [str(item) for item in unique_entries]
    for unique_entry in unique_entries:
        match, score = process.extractOne(unique_entry, unique_entries)
        if score >= 80:
            if unique_entry != match:
                if not is_pcode_diff(df, unique_entry, match):
                    print(f"Match:{unique_entry, match}")


def is_pcode_diff(df, unique_entry, match):
    q1 = df.PCODE[df.NAME == unique_entry]
    q2 = df.PCODE[df.NAME == match]
    if set(q1.unique()) != set(q2.unique()):
        return True
    else:
        return False


def check_string_matching(df, col="NAME"):
    unique_entries = df[col].fillna(0).unique()
    unique_entries = [str(item) for item in unique_entries]
    for unique_entry in unique_entries:
        match, score = process.extractOne(unique_entry, unique_entries)
        if score >= 80:
            if unique_entry != match:
                if col == "NAME":
                    if is_pcode_diff(df, unique_entry, match):
                        print(f"Match:{unique_entry, match}")
                elif col == "BRAND":
                    print(f"Match:{unique_entry, match}")
        else:
            print(f"Error:{unique_entry}")


def run_check(df, col, df_name):
    check_string_matching(df, col)
    input("displayed " + df_name)


name_list = ["corn", "sorghum", "soybean", "sunflower", "wheat"]

for name in name_list:
    df = pd.read_csv("datasets/" + name + ".csv")

    # df = col_to_upper(df, "NAME")
    # df.to_csv("datasets/" + name + ".csv", index=False)

    # run_check(df, 'NAME', unique_entry)
    # coa_name_two(df)
    # input("displayed " + name)

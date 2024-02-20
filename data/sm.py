import pandas as pd
from thefuzz import fuzz, process

"""
Conclusions:
    Canola:
        -- No way of knowing. Maybe should just do the string matching to fix typos.
    Corn:
        --NAME: all are typos
        --BRAND: casing issues
    Sorghum:
        --NAME: only one and is a typo
        --BRAND: casing issues
    Soybean:
        --NAME: pretty confident that they aren't typos, should leave it be. 
        --BRAND: casing issues
    Sunflower:
        --NAME: no occurrences of matched names with diff pcodes 
        --BRAND: casing issues
    Wheat:
        --NAME: all occurences of matched names with diff pcodes looks like
        casing issues.
        --BRAND: casing issues

Course of Action:
    NAME:
        Force unique_entry to uppercase?
        Match the names with same pcode.
        Match the names with diff pcode with Soybean as an exception.
    BRAND:
        Force uppercase in all entries.
"""


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


name_list = ["corn", "sorghum", "soybean", "sunflower", "wheat"]
for unique_entry in name_list:
    df = pd.read_csv("datasets/" + unique_entry + ".csv")
    check_string_matching(df, col='BRAND')
    input("Displayed " + unique_entry)

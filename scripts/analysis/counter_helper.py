import json
import csv
import pandas as pd

def get_csv(path = './Comp370_final_project/data/sentiment_coding/articles_sentiment_coding.csv'):
    return pd.read_csv(path)

def get_uuid_and_sources_dicts():
    uuid_dict = {}
    sources = {}

    with open('./Comp370_final_project/data/stratified_sampling/annotated_full_article_corpus.json', 'r') as f:
        data = json.load(f)

    for j in data:
        src = j['source']
        if src not in sources:
            sources[src] = {
                'types_counts': {},
                'perception_counts': {}
            }

        uuid_dict[j['uuid']] = {
            'date': j['date'],
            'source': src
        }

    return uuid_dict, sources

# total count
def count_types_and_perception(df, custom_condition=lambda row: True):
    # this way we can detect typos by using the dict
    perception_dict = {}
    type_dict = {}

    for _, row in df.iterrows():
        if not custom_condition(row):
            continue

        if row['coding'] in perception_dict:
            perception_dict[row['coding']] += 1
        else:
            perception_dict[row['coding']] = 1

        if row['type'] in type_dict:
            type_dict[row['type']] += 1
        else:
            type_dict[row['type']] = 1
        
    return type_dict, perception_dict

# count per source
def count_perception_and_type_per_source(df, source, uuid_dict):

    return count_types_and_perception(
        df, 
        custom_condition=lambda row: (
            # if the entry with uuid row['uuid']'s source is the same as the source we want
            # then we count it
            uuid_dict[row['uuid']]['source'] == source

            # i'm using this roundabout method because
            # the sentiment_coding csv doesnt have the date and source collumns
            # because i didnt think i'd need them and now
            # it's too late to go back and change the csv without breaking it
            # since i'm already done with my second coding
        )
    )
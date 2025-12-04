import json
import csv
import pandas as pd

def get_csv(path = './Comp370_final_project/data/sentiment_coding/articles_sentiment_coding.csv'):
    return pd.read_csv(path)

def get_uuid_and_sources_dicts():
    uuid_dict = {}
    sources = {}

    str_json = ""
    with open ('./Comp370_final_project/data/stratified_sampling/annotated_full_article_corpus.json', 'r') as f:
        str_json = f.read()
        f.close()

    data = json.loads(str_json)

    for j in data:
        if not (j['source'] in sources):
            sources[j['source']] = {}
            sources[j['source']]['types_counts'] = {}
            sources[j['source']]['perception_counts'] = {}

        uuid_dict[j['uuid']] = \
        {
            'date' : j ['date'],
            'source' : j ['source']
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
            perception_dict[row['coding']] = 0

        if row['type'] in perception_dict:
            type_dict[row['type']] += 1
        else:
            type_dict[row['type']] = 0
        
    return type_dict, perception_dict

# count per source
def count_perception_and_type_per_source(df, source, uuid_dict):

    count_types_and_perception(
        df, 
        custom_condition=lambda row: 
            # if the entry with uuid row['uuid']'s source is the same as the source we want
            # then we count it
            uuid_dict[row['uuid']]['source'] == source

            # i'm using this roundabout method because
            # the sentiment_coding csv doesnt have the date and source collumns
            # because i didnt think i'd need them and now
            # it's too late to go back and change the csv without breaking it
            # since i'm already done with my second coding
        )
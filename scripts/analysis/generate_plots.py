import matplotlib.pyplot as plt
from counter_helper import *
import pandas as pd



def main():
    df = pd.read_csv('./Comp370_final_project/data/sentiment_coding/articles_sentiment_coding.csv')

    uuid_dict, sources = get_uuid_and_sources_dicts()

    for source in sources.keys():
        source_types, source_perceptions = count_perception_and_type_per_source(df, source, uuid_dict)

        sources[source]['types_counts'] = source_types
        sources[source]['perception_counts'] = source_perceptions
    
    type_total, perception_total = count_types_and_perception(df)

if __name__ == "__main__":
    main()
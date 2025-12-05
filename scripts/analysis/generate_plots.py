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

    # types over entire dataset
    plt.figure()
    sorted_types = sorted(type_total.keys(), key=int)
    plt.bar(sorted_types, [type_total[t] for t in sorted_types])
    plt.title('Counts of Types (All Sources)')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


    # perceptions over entire dataset
    plt.figure()
    plt.bar(perception_total.keys(), perception_total.values())
    plt.title('Counts of Perceptions (All Sources)')
    plt.xlabel('Perception')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # per source types bar chart

    types_df = pd.DataFrame({
        source: sources[source]['types_counts'] for source in sources
    }).T

    types_df = types_df.reindex(sorted(types_df.columns, key=int), axis=1)  # sort columns 1–6
    types_df = types_df.fillna(0).astype(int)

    plt.figure()
    types_df.plot(kind='bar')
    plt.title('Type Counts per Source')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # per source perception bar chart
    perceptions_df = pd.DataFrame({
        source: sources[source]['perception_counts'] for source in sources
    }).T.fillna(0).astype(int)

    plt.figure()
    perceptions_df.plot(kind='bar')
    plt.title('Perception Counts per Source')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
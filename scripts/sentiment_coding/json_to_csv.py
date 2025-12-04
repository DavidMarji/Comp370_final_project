# turns the full_article_corpus json file to a csv file ready for another coding
import json
import csv

def main():
    str_json = ""
    with open ('./Comp370_final_project/data/stratified_sampling/annotated_full_article_corpus.json', 'r') as f:
        str_json = f.read()
        f.close()

    data = json.loads(str_json)

    with open ('./Comp370_final_project/data/sentiment_coding/articles_sentiment_coding.csv', 'w') as f:

        # using csv lib to deal with commas inside the text
        writer = csv.writer(f)
        writer.writerow(['uuid', 'title', 'opening', 'type', 'coding'])

        for j in data:
            # surrounded title and snippet in "" since some of them contain commas
            writer.writerow([
                j['uuid'],
                j['title'].replace('\n', ' '),
                j['snippet'].replace('\n', ' '),
                j['type'],
                ''
            ])
        
        f.close()


if __name__ == "__main__":
    main()
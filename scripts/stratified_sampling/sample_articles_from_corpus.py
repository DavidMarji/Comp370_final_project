import json
import random

input = "data/stratified_sampling/unannotated_full_article_corpus.json"
output = "data/stratified_sampling/unannotated_sample_articles.json"

with open(input, "r") as infile, open(output, "w") as outfile:

    percent = 0.4 # 200/500 = 0.4
    source_lengths = {}
    corpus = json.load(infile)
    by_source = {}
    sample = []
    
    for article in corpus:

        if article["source"] not in by_source.keys():
            by_source[article["source"]] = []
            source_lengths[article["source"]] = 0
        
        by_source[article["source"]].append(article)
        source_lengths[article["source"]] += 1
    
    for key in by_source.keys():

        sample.extend(random.sample(by_source[key], int(source_lengths[key]*percent)))

    random.shuffle(sample)
    
    json.dump(sample, outfile, indent=4, ensure_ascii=False)
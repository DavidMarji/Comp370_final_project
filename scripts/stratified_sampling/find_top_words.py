import json
import math
import re
from collections import Counter, defaultdict
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

input = "data/stratified_sampling/annotated_full_article_corpus.json"
output = "docs/top_words_per_type.json"

with open(input, "r") as infile, open(output, "w") as outfile:

    corpus = json.load(infile)

    tf = defaultdict(Counter)
    vocab = defaultdict(set)

    stop_words = list(ENGLISH_STOP_WORDS.union(["trump", "president", "donald"]))

    def tokenize(text):
        tokens = re.findall(r"[a-zA-Z']+", text.lower())
        return [
            t for t in tokens
            if t not in stop_words and len(t) > 2
        ]

    for article in corpus:
        c = article["type"]
        title = article.get("title", "") or ""
        desc = article.get("description", "") or ""
        snip = article.get("snippet", "") or ""
        text = f"{title} {desc} {snip}"

        tokens = tokenize(text)
        unique_tokens = set(tokens)
        tf[c].update(unique_tokens)
        vocab[c].update(unique_tokens)


    categories = sorted(tf.keys())
    N = len(categories)

    df = Counter()
    for c in categories:
        for w in vocab[c]:
            df[w] += 1

    results = {}

    for c in categories:
        scores = {}
        for w, count in tf[c].items():
            idf = math.log(N / df[w])
            scores[w] = count * idf

        top10 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
        results[int(c)] = [
            {"word": w, "score": s} for w, s in top10
        ]

    json.dump(results, outfile, indent=4, ensure_ascii=False)
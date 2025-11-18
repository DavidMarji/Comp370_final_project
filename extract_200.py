import json

INPUT_FILE = "trump_articles_partial.json"
OUTPUT_FILE = "trump_articles_200_open_coding.json"

def load_articles(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def convert_for_open_coding(articles):
    cleaned = []
    for a in articles[:200]:  # get first 200
        cleaned.append({
            "title": a.get("title"),
            "description": a.get("description"),
            "opening": a.get("snippet")  # This is the article’s opening text
        })
    return cleaned

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    raw_articles = load_articles(INPUT_FILE)
    cleaned = convert_for_open_coding(raw_articles)
    save_json(cleaned, OUTPUT_FILE)

    print(f"Created {OUTPUT_FILE} with {len(cleaned)} cleaned articles.")

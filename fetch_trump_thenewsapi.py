#!/usr/bin/env python3
"""
Fetch EXACTLY 500 Trump-related articles from TheNewsAPI across selected North American outlets.
Saves progress every 50 new articles.
Setup: pip install requests tqdm pandas 
Run: 
export NEWSAPI_KEY="YOUR_API_KEY" 
python fetch_trump_thenewsapi.py
"""


import os
import requests
import time
import json
import pandas as pd
from tqdm import tqdm

API_KEY = os.getenv("NEWSAPI_KEY")
if not API_KEY:
    raise SystemExit("Please set environment variable NEWSAPI_KEY")

BASE_URL = "https://api.thenewsapi.com/v1/news/all"

DOMAINS = [
    "nytimes.com",
    "washingtonpost.com",
    "cbc.ca",
    "apnews.com",
    "reuters.com",
    "npr.org",
    "pbs.org",
    "wsj.com",
    "nationalpost.com",
    "foxnews.com"
]

QUERY = "Trump OR \"Donald Trump\""

PARTIAL_JSON = "trump_articles_partial.json"
PARTIAL_CSV = "trump_articles_partial.csv"


def fetch_page(page, limit=100):
    params = {
        "api_token": API_KEY,
        "search": QUERY,
        "domains": ",".join(DOMAINS),
        "language": "en",
        "limit": limit,
        "page": page
    }
    r = requests.get(BASE_URL, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def save_partial(collected_dict):
    data = list(collected_dict.values())

    # Save JSON
    with open(PARTIAL_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Save CSV
    df = pd.DataFrame([
        {
            "title": a.get("title"),
            "description": a.get("description"),
            "url": a.get("url"),
            "source": a.get("source"),
            "published_at": a.get("published_at"),
            "snippet": a.get("snippet")
        } for a in data
    ])
    df.to_csv(PARTIAL_CSV, index=False)

    print(f"[Partial Save] Saved {len(data)} articles.")


def load_existing_articles():
    """Load previously saved partial articles, if any."""
    if not os.path.exists(PARTIAL_JSON):
        print("No previous partial file found. Starting fresh.")
        return {}

    try:
        with open(PARTIAL_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)

        collected = {a["url"]: a for a in data if "url" in a}
        print(f"Loaded {len(collected)} existing articles.")
        return collected

    except Exception as e:
        print(f"Failed to load partial file, starting fresh. Error: {e}")
        return {}


def collect_until_500():
    target = 500
    collected = load_existing_articles()
    last_saved_count = len(collected)

    page = 1
    pbar = tqdm(total=target, desc="Collecting articles")
    pbar.update(len(collected))

    while len(collected) < target:
        try:
            data = fetch_page(page)
        except requests.exceptions.HTTPError as e:
            print(f"API error on page {page}: {e}")
            break

        articles = data.get("data", [])
        if not articles:
            print("Reached end of available articles early.")
            break

        added = 0
        for a in articles:
            url = a.get("url")
            if url and url not in collected:
                collected[url] = a
                added += 1
                pbar.update(1)

                # Save every +50 articles
                if len(collected) // 50 > last_saved_count // 50:
                    save_partial(collected)
                    last_saved_count = len(collected)

                if len(collected) >= target:
                    break

        

        page += 1
        time.sleep(0.8)

    pbar.close()

    # enforce exactly 500 if overshoot
    collected_list = list(collected.values())
    if len(collected_list) > target:
        collected_list = collected_list[:target]

    print(f"Final count: {len(collected_list)} articles.")
    return collected_list


def save_final(articles, json_path="trump_articles_500.json",
               csv_path="trump_articles_500.csv"):

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame([
        {
            "title": a.get("title"),
            "description": a.get("description"),
            "url": a.get("url"),
            "source": a.get("source"),
            "published_at": a.get("published_at"),
            "snippet": a.get("snippet")
        } for a in articles
    ])
    df.to_csv(csv_path, index=False)

    print(f"Saved final JSON → {json_path}")
    print(f"Saved final CSV  → {csv_path}")


if __name__ == "__main__":
    articles = collect_until_500()
    save_final(articles)

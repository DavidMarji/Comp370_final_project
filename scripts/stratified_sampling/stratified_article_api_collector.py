import time
import random
import json
import re
import requests

API_BASE_URL = "https://api.thenewsapi.com/v1/news/all"

PUBLISHED_AFTER = "2023-11-20"
PUBLISHED_BEFORE = "2025-11-19"

OUTLETS = [
    {
        "outlet_name": "The Washington Post",
        "domain": "washingtonpost.com",
        "target_n": 70,
    },
    {
        "outlet_name": "ABC News",
        "domain": "abcnews.go.com",
        "target_n": 70,
    },
    {
        "outlet_name": "Associated Press",
        "domain": "apnews.com",
        "target_n": 70,
    },
    {
        "outlet_name": "Fox News",
        "domain": "foxnews.com",
        "target_n": 70,
    },
    {
        "outlet_name": "New York Post",
        "domain": "nypost.com",
        "target_n": 70,
    },
    {
        "outlet_name": "CBC News",
        "domain": "cbc.ca",
        "target_n": 30,
    },
    {
        "outlet_name": "Global News",
        "domain": "globalnews.ca",
        "target_n": 30,
    },
    {
        "outlet_name": "CTV News",
        "domain": "ctvnews.ca",
        "target_n": 30,
    },
    {
        "outlet_name": "National Post",
        "domain": "nationalpost.com",
        "target_n": 30,
    },
    {
        "outlet_name": "Financial Post",
        "domain": "financialpost.com",
        "target_n": 30,
    },
]

OUTPUT_JSON = "data/stratified_sampling/unannotated_full_article_corpus.json"

GLOBAL_MAX_PAGES_PER_QUERY = 150


def article_mentions_trump_word(article):

    pattern = re.compile(r"\bTrump\b")
    fields = [
        article.get("title") or "",
        article.get("snippet") or "",
        article.get("description") or "",
    ]

    return any(pattern.search(text) for text in fields)


def safe_request(url, params):

    while True:
        time.sleep(1)
        resp = requests.get(url, params=params)

        if resp.status_code == 429:

            print("Too many requests, sleeping for 60 seconds")
            time.sleep(60)
            continue

        if resp.status_code != 200:
            print(f"Request failed with status {resp.status_code}: {resp.text}",)
            return None

        return resp.json()


def fetch_all_articles_for_domain(api_token, domain, search_query, published_after, published_before, language = "en"):

    all_articles = []

    params = {
        "api_token": api_token,
        "search": search_query,
        "search_fields": "title,main_text",
        "domains": domain,
        "language": language,
        "published_after": published_after,
        "published_before": published_before,
        "page": 1,
    }

    page = 1

    while True:
        params["page"] = page
        print(f"Fetching from {domain} at page {page}...")
        data = safe_request(API_BASE_URL, params)

        if data is None:
            print(f"Stopping pagination on {domain} early due to error")
            break

        items = data.get("data", [])
        all_articles.extend(items)

        if page >= GLOBAL_MAX_PAGES_PER_QUERY:
            print(f"Reached max pages ({GLOBAL_MAX_PAGES_PER_QUERY} on {domain})")
            break

        page += 1

    print(f"Fetched {len(all_articles)} articles total from {domain}")
    return all_articles


def sample_articles(articles, n, seed = 42):

    if seed is not None:
        random.seed(seed)

    if len(articles) <= n:
        print("Not enough articles to perform sample")
        return articles

    return random.sample(articles, n)


def main():
    api_token = "ABCDEFG"

    all_selected = []

    for outlet_cfg in OUTLETS:
        domain = outlet_cfg["domain"]
        outlet_name = outlet_cfg["outlet_name"]
        target_n = outlet_cfg["target_n"]

        print(f"\n========== {outlet_name} ({domain}) ==========")

        all_articles_for_domain = fetch_all_articles_for_domain(
            api_token=api_token,
            domain=domain,
            search_query='"Donald Trump"',
            published_after=PUBLISHED_AFTER,
            published_before=PUBLISHED_BEFORE,
            language="en",
        )

        if not all_articles_for_domain:
            print(f"No articles found for {outlet_name}")
            continue

        filtered_articles = [art for art in all_articles_for_domain if article_mentions_trump_word(art)]

        if not filtered_articles:
            print(f"No articles found mentioning Donald Trump in {outlet_name}")
            continue

        selected_articles = sample_articles(filtered_articles, target_n)

        for art in selected_articles:
            enriched = {
                "uuid": art.get("uuid"),
                "title": art.get("title"),
                "description": art.get("description"),
                "snippet": art.get("snippet"),
                "source": outlet_name,
                "date": art.get("published_at")
            }
            all_selected.append(enriched)

        print(f"Selected {len(selected_articles)} articles from {outlet_name} out of {target_n} targetted")

    print("\n========== SUMMARY ==========")
    print(f"Total selected articles: {len(all_selected)}")

    with open(OUTPUT_JSON, "w") as outfile:
        json.dump(all_selected, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
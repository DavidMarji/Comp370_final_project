import json
from datetime import datetime, date
from collections import Counter, defaultdict

import matplotlib.pyplot as plt

input = "temp.json"

with open(input, "r") as infile:

    corpus = json.load(infile)

    plt.rcParams.update({
        "axes.labelsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 11,
    })

    SOURCE_ORDER = [
        "CBC",
        "The Washington Post",
        "ABC News",
        "Global News",
        "Associated Press",
        "CTV News",
        "Financial Post",
        "National Post",
        "New York Post",
        "Fox News",
    ]

    quarter_ranges = [
        (date(2023, 11, 20), date(2024, 2, 19)),
        (date(2024, 2, 20), date(2024, 5, 19)),
        (date(2024, 5, 20), date(2024, 8, 19)),
        (date(2024, 8, 20), date(2024, 11, 19)),
        (date(2024, 11, 20), date(2025, 2, 19)),
        (date(2025, 2, 20), date(2025, 5, 19)),
        (date(2025, 5, 20), date(2025, 8, 19)),
        (date(2025, 8, 20), date(2025, 11, 19)),
    ]

    def get_quarter(d):
        for i, (start, end) in enumerate(quarter_ranges):
            if start <= d <= end:
                return i
        return 0

    topics_overall = Counter()
    quarter_type = [Counter() for _ in range(8)]
    quarter_sentiment = [Counter() for _ in range(8)]
    source_topic = defaultdict(Counter)

    for article in corpus:
        t = article["type"]
        s = article["sentiment"]
        src = article["source"]

        topics_overall[t] += 1

        d = datetime.fromisoformat(article["date"].replace("Z", "+00:00")).date()
        q = get_quarter(d)
        quarter_type[q][t] += 1
        quarter_sentiment[q][s] += 1

        source_topic[src][t] += 1

    topics = sorted(topics_overall.keys())
    sentiments = sorted({s for qs in quarter_sentiment for s in qs})

    topic_colors = [plt.cm.Pastel1(i % 9) for i in range(len(topics))]

    sentiment_palette = ["darkgreen", "darkblue", "darkorange", "purple"]
    sentiment_colors = {}
    for i, s in enumerate(sentiments):
        sentiment_colors[s] = sentiment_palette[i % len(sentiment_palette)]
    if "Neutral" in sentiments:
        sentiment_colors["Neutral"] = "black"
    if "Negative" in sentiments:
        sentiment_colors["Negative"] = "red"

    plt.figure(figsize=(6, 4))

    xs = range(len(topics))
    for i, t in enumerate(topics):
        plt.bar(
            i,
            topics_overall[t],
            color=topic_colors[i],
            label=f"Topic {t}",
        )

    plt.xlabel("Topic")
    plt.ylabel("Count")
    plt.xticks(xs, [str(t) for t in topics])
    plt.legend()

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    quarters = range(8)
    bottoms = [0.0] * 8

    for i, t in enumerate(topics):
        heights = []
        for q in quarters:
            total = sum(quarter_type[q].values())
            if total == 0:
                heights.append(0.0)
            else:
                heights.append(quarter_type[q][t] / total)
        ax2.bar(
            [q + 1 for q in quarters],
            heights,
            bottom=bottoms,
            color=topic_colors[i],
            label=f"Topic {t}",
            edgecolor="white",
            linewidth=0.5,
        )
        bottoms = [b + h for b, h in zip(bottoms, heights)]

    for s in sentiments:
        ys = []
        for q in quarters:
            total = sum(quarter_sentiment[q].values())
            if total == 0:
                ys.append(0.0)
            else:
                ys.append(quarter_sentiment[q][s] / total)
        ax2.plot(
            [q + 1 for q in quarters],
            ys,
            marker="o",
            linestyle="-",
            color=sentiment_colors[s],
            label=s,
            linewidth=2,
        )

    ax2.set_xlabel("Quarter")
    ax2.set_ylabel("Proportion")

    handles, labels = ax2.get_legend_handles_labels()
    ax2.legend(
        handles,
        labels,
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    fig2.tight_layout(rect=[0, 0, 0.82, 1])

    fig3, ax3 = plt.subplots(figsize=(12, 4))

    ordered_sources = SOURCE_ORDER
    x_positions = list(range(len(ordered_sources)))
    bottoms = [0.0] * len(ordered_sources)

    for j, t in enumerate(topics):
        heights = []
        for src in ordered_sources:
            c = source_topic[src]
            total = sum(c.values())
            if total == 0:
                heights.append(0.0)
            else:
                heights.append(c[t] / total)
        ax3.bar(
            x_positions,
            heights,
            width=1.0,
            bottom=bottoms,
            color=topic_colors[j],
            label=f"Topic {t}",
            edgecolor="white",
            linewidth=0.5,
        )
        bottoms = [b + h for b, h in zip(bottoms, heights)]

    ax3.set_xlabel("Source")
    ax3.set_ylabel("Topic proportion")
    ax3.set_xticks(x_positions)
    ax3.set_xticklabels(ordered_sources, rotation=45, ha="right")

    ax3.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    fig3.tight_layout(rect=[0, 0, 0.82, 1])

    plt.show()
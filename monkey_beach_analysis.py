import json
import numpy as np
import matplotlib.pyplot as plt

# Looks through the json file and grabs the text. Reminder to append white spaces !

pages = []
with open("monkey_beach_pages.jsonl") as f:
    for line in f:
        obj = json.loads(line)
        if obj["text"].strip():
            pages.append(obj)

# Define words the nlp detects

land_words = [
    "water", "inlet", "salmon", "cedar", "shore", "kitamaat",
    "ocean", "forest", "tide", "beach", "river", "mountain",
    "sea", "coast", "creek", "rain", "mud", "land", "trees", "island"
]

fp_words = [
    "haisla", "ceremony", "elder", "ancestor", "potlatch",
    "spirit", "b'gwus", "clan", "tradition", "chief", "feast",
    "drum", "raven", "eagle", "totem", "medicine", "healing",
    "prayer", "song", "mask"
]

# Counting amount of words per page

land_counts = []
fp_counts = []
page_nums = []

for page in pages:
    text = page["text"].lower()
    words = text.split()

    land_count = sum(1 for w in words if any(lw in w for lw in land_words))
    fp_count   = sum(1 for w in words if any(fw in w for fw in fp_words))

    land_counts.append(land_count)
    fp_counts.append(fp_count)
    page_nums.append(page["page"])

# Rolling avg PER PAGE

def rolling_avg(data, window=10):
    return np.convolve(data, np.ones(window) / window, mode="same")

land_smooth = rolling_avg(land_counts)
fp_smooth   = rolling_avg(fp_counts)

# Plot values

plt.figure(figsize=(14, 6))

plt.plot(page_nums, land_smooth, label="Land / Place Language",
         color="#2E8B57", linewidth=2)
plt.plot(page_nums, fp_smooth,   label="First Peoples Cultural Language",
         color="#8B4513", linewidth=2)

plt.title("Semantic Field Distribution in Monkey Beach — Eden Robinson",
          fontsize=14, fontweight="bold")
plt.xlabel("Page Number", fontsize=11)
plt.ylabel("Word Frequency  (10-page rolling average)", fontsize=11)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig("monkey_beach_analysis.png", dpi=150)
plt.show()
print("Saved → monkey_beach_analysis.png")

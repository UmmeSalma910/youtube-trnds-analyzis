import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load the category ID JSON
with open("CA_category_id.json", "r") as f:
    data = json.load(f)

# Extract ID and title from each item
categories = {
    int(item["id"]): item["snippet"]["title"]
    for item in data["items"]
}

# Convert to a DataFrame
category_df = pd.DataFrame(list(categories.items()), columns=["category_id", "category_name"])
print(category_df.head())


# Top 10 most viewed videos
top_views = df.sort_values(by='views', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_views, y='title', x='views', palette='viridis')
plt.title("Top 10 Most Viewed YouTube Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

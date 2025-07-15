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

# Load YouTube video data
df = pd.read_csv("USvideos.csv")

# Merge with category names
df = df.merge(category_df, how="left", on="category_id")

# Check result
print(df[["title", "category_id", "category_name"]].head())


# Top 10 most viewed videos
top_views = df.sort_values(by='views', ascending=False).head(10)


avg_views = df.groupby('category_name')['views'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_views.values, y=avg_views.index, palette='coolwarm')
plt.title("Average Views by Video Category")
plt.xlabel("Average Views")
plt.ylabel("Category")
plt.tight_layout()
plt.show()





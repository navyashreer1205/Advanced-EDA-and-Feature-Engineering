import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("dataset/final_feature_engineered_dataset.csv")

# ---------- Graph 1 ----------
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    y="Product",
    order=df["Product"].value_counts().index,
    color="steelblue"
)

plt.title("Number of Orders by Product")
plt.tight_layout()
plt.savefig("output/product_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------- Graph 2 ----------
plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="UnitPrice",
    bins=12,
    kde=True,
    color="green"
)

plt.title("Distribution of Unit Price")
plt.tight_layout()
plt.savefig("output/unit_price_histogram.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------- Graph 3 ----------
plt.figure(figsize=(8,4))

sns.boxplot(
    data=df,
    x="UnitPrice",
    color="orange"
)

plt.title("Boxplot of Unit Price")
plt.tight_layout()
plt.savefig("output/unit_price_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# IQR METHOD
# -----------------------------

Q1 = df["UnitPrice"].quantile(0.25)
Q3 = df["UnitPrice"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nQ1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Lower Limit =", lower)
print("Upper Limit =", upper)

outliers = df[
    (df["UnitPrice"] < lower) |
    (df["UnitPrice"] > upper)
]

print("\nTotal Outliers:", len(outliers))

# Remove outliers
df_clean = df[
    (df["UnitPrice"] >= lower) &
    (df["UnitPrice"] <= upper)
]

print("Original Shape:", df.shape)
print("Clean Shape:", df_clean.shape)

df_clean.to_csv(
    "dataset/final_dataset_after_iqr.csv",
    index=False
)

print("\nIQR dataset saved successfully!")

# =====================================
# PHASE 7 : FEATURE ENGINEERING
# =====================================

# Create a copy of the cleaned dataset
feature_df = df_clean.copy()

# Feature 1: Price Per Item
feature_df["PricePerItem"] = (
    feature_df["TotalPrice"] / feature_df["Quantity"]
).round(2)

# Feature 2: High Value Order
feature_df["HighValueOrder"] = (
    feature_df["TotalPrice"] > 1000
).astype(int)

# Fix incomplete dates
feature_df["Date"] = (
    feature_df["Date"].astype(str)
    .str.replace(r"(\d{4}-\d{2}-)0$", r"\g<1>01", regex=True)
)

# Feature 3: Order Month
feature_df["OrderMonth"] = pd.to_datetime(
    feature_df["Date"],
    errors="coerce"
).dt.month

# Save final dataset
feature_df.to_csv(
    "dataset/final_feature_engineered_dataset.csv",
    index=False
)

# Display results
print("\n===== FEATURE ENGINEERING COMPLETED =====\n")

print(feature_df[
    ["TotalPrice","Quantity","PricePerItem",
     "HighValueOrder","OrderMonth"]
].head())

print("\nNew Columns:")
print(feature_df.columns.tolist())

print("\nFinal Shape:", feature_df.shape)
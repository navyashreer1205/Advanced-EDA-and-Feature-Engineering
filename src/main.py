import pandas as pd

# Read Excel without headers
raw = pd.read_excel(
    "dataset/Dataset for Data Analytics-decodelabp1.xlsx",
    header=None
)

# Keep only the required columns
raw = raw.iloc[1:, [0, 3, 6, 8, 9, 14, 15, 16, 18]]

raw.columns = [
    "Merged", "Product", "Quantity", "UnitPrice",
    "ShippingInfo", "ItemsInCart", "CouponCode",
    "ReferralSource", "TotalPrice"
]

# Extract OrderID, Date and CustomerID
raw["OrderID"] = raw["Merged"].str.extract(r"(ORD\d+)")
raw["Date"] = raw["Merged"].str.extract(r"(\d{4}-\d{2}-\d)")
raw["CustomerID"] = raw["Merged"].str.extract(r"(C\d+)")

# Extract Shipping Address, Order Status and Tracking Number
raw["ShippingAddress"] = raw["ShippingInfo"].str.extract(r"^(\d+\sMain)")
raw["OrderStatus"] = raw["ShippingInfo"].str.extract(r"(Shipped|Delivered|Returned|Pending|Cancelled)")
raw["TrackingNumber"] = raw["ShippingInfo"].str.extract(r"(TRK\d+)")

# Final dataframe
df = raw[[
    "OrderID", "Date", "CustomerID", "Product",
    "Quantity", "UnitPrice", "ShippingAddress",
    "OrderStatus", "TrackingNumber", "ItemsInCart",
    "CouponCode", "ReferralSource", "TotalPrice"
]]

# Convert numeric columns
for col in ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Save cleaned dataset
df.to_csv("dataset/final_cleaned_dataset.csv", index=False)

print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing categorical values
df["OrderStatus"] = df["OrderStatus"].fillna("Pending")
df["TrackingNumber"] = df["TrackingNumber"].fillna("Not Assigned")
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Save updated dataset
df.to_csv("dataset/final_cleaned_dataset.csv", index=False)

print("\nAfter Filling Missing Values:")
print(df.isnull().sum())
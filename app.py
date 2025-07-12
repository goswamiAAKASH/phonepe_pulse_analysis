import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="📊 PhonePe Pulse Dashboard", layout="wide")
st.title("📱 PhonePe Pulse - Data Insights Dashboard")

# Load CSVs
def load_data():
    df_txn = pd.read_csv("aggregated_transaction.csv")
    df_user = pd.read_csv("aggregated_user.csv")
    df_ins = pd.read_csv("aggregated_insurance.csv")
    df_map_user = pd.read_csv("map_user.csv")
    df_map_ins = pd.read_csv("map_insurance.csv")
    df_top_txn = pd.read_csv("top_transaction.csv")
    df_top_user = pd.read_csv("top_user.csv")
    return df_txn, df_user, df_ins, df_map_user, df_map_ins, df_top_txn, df_top_user

@st.cache_data
def cached_data():
    return load_data()

df_txn, df_user, df_ins, df_map_user, df_map_ins, df_top_txn, df_top_user = cached_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
years = sorted(df_txn["year"].unique())
states = sorted(df_txn["state"].unique())
year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
state = st.sidebar.selectbox("Select State", states)

# Apply filters to data
df_txn_filtered = df_txn[(df_txn["year"] == year) & (df_txn["state"] == state)]
df_user_filtered = df_user[(df_user["year"] == year) & (df_user["state"] == state)]
df_ins_filtered = df_ins[(df_ins["year"] == year) & (df_ins["state"] == state)]
df_map_user_filtered = df_map_user[(df_map_user["year"] == year) & (df_map_user["state"] == state)]
df_map_ins_filtered = df_map_ins[(df_map_ins["year"] == year) & (df_map_ins["state"] == state)]
df_top_txn_filtered = df_top_txn[(df_top_txn["year"] == year) & (df_top_txn["state"] == state)]
df_top_user_filtered = df_top_user[(df_top_user["year"] == year) & (df_top_user["state"] == state)]

# Chart 1 - Top 10 Transaction Types in selected state/year
st.subheader("📌 Chart 1: Top Transaction Types in State")
top_txn_types = df_txn_filtered.groupby("transaction_type")["count"].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_txn_types.values, y=top_txn_types.index, ax=ax1, palette="Blues_r")
ax1.set_xlabel("Total Transactions")
st.pyplot(fig1)

# Chart 2 - Top Smartphone Brands
st.subheader("📱 Chart 2: Smartphone Brand Usage in State")
top_brands = df_user_filtered.groupby("brand")["count"].sum().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_brands.index, y=top_brands.values, ax=ax2, palette="Set2")
ax2.set_ylabel("User Count")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Chart 3 - Year-wise Transaction Volume (unfiltered)
st.subheader("📈 Chart 3: Transaction Volume Over Years")
year_trend = df_txn.groupby("year")["amount"].sum()
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(year_trend.index, year_trend.values, marker='o', linestyle='-', color='blue')
ax3.set_title("Transaction Volume Over Years")
ax3.set_xlabel("Year")
ax3.set_ylabel("Amount")
ax3.grid(True)
st.pyplot(fig3)

# Chart 4 - App Opens vs Registered Users (Filtered)
st.subheader("📍 Chart 4: App Opens vs Registered Users in State")
app_user = df_map_user_filtered.groupby("district")[["registered_users", "app_opens"]].sum().reset_index()
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.scatter(app_user["registered_users"], app_user["app_opens"], color='green', alpha=0.6)
for i in range(len(app_user)):
    ax4.text(app_user["registered_users"][i], app_user["app_opens"][i], app_user["district"][i], fontsize=7)
ax4.set_xlabel("Registered Users")
ax4.set_ylabel("App Opens")
ax4.set_title(f"App Opens vs Registered Users in {state} ({year})")
st.pyplot(fig4)

# Chart 5 - Transaction vs Insurance in State
txn_sum = df_txn_filtered["amount"].sum()
ins_sum = df_ins_filtered["amount"].sum()
st.subheader("🧾 Chart 5: Transaction vs Insurance Volume (State)")
fig5, ax5 = plt.subplots(figsize=(6, 4))
ax5.bar(["Transactions", "Insurance"], [txn_sum, ins_sum], color=["skyblue", "orange"])
ax5.set_ylabel("Amount")
ax5.set_title(f"Transactions vs Insurance Volume in {state} ({year})")
st.pyplot(fig5)

# Chart 6 - Top 10 Pincodes in State
top_pins = df_top_txn_filtered.groupby("pincode")["count"].sum().sort_values(ascending=False).head(10)
st.subheader("📮 Chart 6: Top 10 Pincodes by Transactions")
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_pins.index.astype(str), y=top_pins.values, ax=ax6, palette="Greens_r")
ax6.set_xlabel("Pincode")
ax6.set_ylabel("Transactions")
ax6.set_title(f"Top 10 Pincodes in {state} ({year})")
plt.xticks(rotation=45)
st.pyplot(fig6)

# Chart 7 - Top 10 Districts by Insurance
st.subheader("🏥 Chart 7: Top Districts by Insurance Transactions")
districts = df_map_ins_filtered.groupby("district")["count"].sum().sort_values(ascending=False).head(10)
fig7, ax7 = plt.subplots(figsize=(10, 5))
sns.barplot(x=districts.values, y=districts.index, ax=ax7, palette="Purples_r")
ax7.set_xlabel("Insurance Transactions")
ax7.set_title(f"Top 10 Districts in {state} ({year})")
st.pyplot(fig7)

# Chart 8 - Insurance % of Transactions in State
st.subheader("📊 Chart 8: Insurance % of Transactions in State")
ratio = (ins_sum / txn_sum) * 100 if txn_sum > 0 else 0
fig8, ax8 = plt.subplots(figsize=(5, 4))
ax8.bar(["Insurance %"], [ratio], color="magenta")
ax8.set_ylabel("% of Transaction Volume")
ax8.set_title(f"Insurance Adoption Rate in {state} ({year})")
st.pyplot(fig8)

# Footer
st.markdown("---")
st.caption("📊 Built by Aakash Goswami | Streamlit + CSV | PhonePe Pulse Project")
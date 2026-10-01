import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# Title
st.title("🛒 E-Commerce Customer Segmentation Dashboard")
st.markdown("### RFM Analysis + K-Means Clustering")

# Load data
rfm = pd.read_csv("rfm_final.csv")

# Metrics
total_customers = rfm.shape[0]
total_revenue = rfm['Monetary'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Customers", total_customers)
col2.metric("Total Revenue", f"£{total_revenue:,.2f}")

st.markdown("---")

# Cluster Distribution
st.subheader("Customer Distribution by Cluster")
fig1, ax1 = plt.subplots()
sns.countplot(x='Cluster_Name', data=rfm, palette='viridis', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Cluster Summary
st.subheader("Cluster-wise Average RFM")
cluster_summary = rfm.groupby('Cluster_Name')[['Recency', 'Frequency', 'Monetary']].mean().round(2)
st.dataframe(cluster_summary)

# Scatter Plot
st.subheader("Recency vs Monetary")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(x='Recency', y='Monetary', hue='Cluster_Name', data=rfm, palette='viridis', ax=ax2)
st.pyplot(fig2)
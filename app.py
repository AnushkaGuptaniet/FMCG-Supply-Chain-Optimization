
import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.ensemble import RandomForestClassifier

# -------------------------------------
# PAGE CONFIG
# -------------------------------------

st.set_page_config(
    page_title="FMCG Supply Chain Dashboard",
    page_icon="📦",
    layout="wide"
)

# -------------------------------------
# LOAD DATA
# -------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "dataset/feature_engineered_fmcg.csv"
    )

df = load_data()

# -------------------------------------
# TRAIN MODEL
# -------------------------------------

@st.cache_resource
def train_model():

    data = df.copy()

    mapping = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    data["Demand_Category"] = (
        data["Demand_Category"]
        .map(mapping)
    )

    X = data[
        [
            "Inventory_Level",
            "Price",
            "Promotion_Flag"
        ]
    ]

    y = data["Demand_Category"]

    model = RandomForestClassifier(
        n_estimators=50,
        max_depth=10,
        random_state=42
    )

    model.fit(X, y)

    return model

model = train_model()

# -------------------------------------
# TITLE
# -------------------------------------

st.title("📦 FMCG Supply Chain Optimization Dashboard")

st.markdown(
"""
Analyze inventory, sales demand, promotion impact,
and predict product demand using Machine Learning.
"""
)

# -------------------------------------
# SIDEBAR FILTERS
# -------------------------------------

st.sidebar.header("Filters")

selected_zone = st.sidebar.multiselect(
    "Select Zone",
    options=df["zone"].unique(),
    default=df["zone"].unique()
)

selected_demand = st.sidebar.multiselect(
    "Demand Category",
    options=df["Demand_Category"].unique(),
    default=df["Demand_Category"].unique()
)

filtered_df = df[
    (df["zone"].isin(selected_zone))
    &
    (df["Demand_Category"].isin(selected_demand))
]

# -------------------------------------
# KPI CARDS
# -------------------------------------

st.subheader("Business KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Sales",
    round(
        filtered_df["Sales_Quantity"].mean(),
        2
    )
)

col3.metric(
    "Average Inventory",
    round(
        filtered_df["Inventory_Level"].mean(),
        2
    )
)

col4.metric(
    "Average Price",
    round(
        filtered_df["Price"].mean(),
        2
    )
)

st.divider()

# -------------------------------------
# DATA PREVIEW
# -------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# -------------------------------------
# DEMAND DISTRIBUTION
# -------------------------------------

st.subheader("Demand Category Distribution")

demand_count = (
    filtered_df["Demand_Category"]
    .value_counts()
    .reset_index()
)

demand_count.columns = [
    "Demand_Category",
    "Count"
]

fig1 = px.bar(
    demand_count,
    x="Demand_Category",
    y="Count",
    title="Demand Category Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -------------------------------------
# PROMOTION IMPACT
# -------------------------------------

st.subheader("Promotion Impact")

promo_data = (
    filtered_df
    .groupby("Promotion_Flag")
    ["Sales_Quantity"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    promo_data,
    x="Promotion_Flag",
    y="Sales_Quantity",
    title="Average Sales by Promotion"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -------------------------------------
# INVENTORY VS SALES
# -------------------------------------

st.subheader("Inventory vs Sales")

fig3 = px.scatter(
    filtered_df,
    x="Inventory_Level",
    y="Sales_Quantity",
    color="Demand_Category",
    title="Inventory vs Sales"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -------------------------------------
# REGION ANALYSIS
# -------------------------------------

st.subheader("Zone Distribution")

zone_data = (
    filtered_df["zone"]
    .value_counts()
    .reset_index()
)

zone_data.columns = [
    "Zone",
    "Count"
]

fig4 = px.bar(
    zone_data,
    x="Zone",
    y="Count",
    title="Warehouse Zone Distribution"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# -------------------------------------
# TOP PRODUCTS
# -------------------------------------

st.subheader("Top Products")

top_products = (
    filtered_df
    .groupby("Product_Name")
    ["Sales_Quantity"]
    .sum()
    .reset_index()
    .sort_values(
        by="Sales_Quantity",
        ascending=False
    )
    .head(10)
)

fig5 = px.bar(
    top_products,
    x="Product_Name",
    y="Sales_Quantity",
    title="Top 10 Products by Sales"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# -------------------------------------
# DOWNLOAD DATA
# -------------------------------------

st.subheader("Download Data")

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_fmcg_data.csv",
    mime="text/csv"
)

# -------------------------------------
# DEMAND PREDICTION
# -------------------------------------

st.divider()

st.header("🔮 Demand Prediction")

col1, col2 = st.columns(2)

with col1:
    inventory = st.number_input(
        "Inventory Level",
        min_value=0,
        value=1000
    )

with col2:
    price = st.number_input(
        "Price",
        min_value=0.0,
        value=100.0
    )

promotion = st.selectbox(
    "Promotion Running?",
    [0, 1]
)

if st.button("Predict Demand"):

    prediction = model.predict(
        [[inventory, price, promotion]]
    )

    labels = {
        0: "Low Demand",
        1: "Medium Demand",
        2: "High Demand"
    }

    st.success(
        f"Predicted Demand: {labels[prediction[0]]}"
    )

# -------------------------------------
# FOOTER
# -------------------------------------

st.divider()

st.caption(
    "FMCG Supply Chain Optimization Project"
)


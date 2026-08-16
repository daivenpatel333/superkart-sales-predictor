
import streamlit as st
import requests

st.title("SuperKart Product Store Sales Predictor")

# Product inputs
Product_Weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=12.66
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=0.05
)

Product_Type = st.selectbox(
    "Product Type",
    [
        "Baking Goods",
        "Breads",
        "Breakfast",
        "Canned",
        "Dairy",
        "Frozen Foods",
        "Fruits and Vegetables",
        "Health and Hygiene",
        "Household",
        "Meat",
        "Others",
        "Seafood",
        "Snack Foods",
        "Soft Drinks",
        "Starchy Foods"
    ]
)

Product_MRP = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=100.0
)

# Store inputs
Store_Establishment_Year = st.number_input(
    "Store Establishment Year",
    min_value=1980,
    max_value=2026,
    value=1999
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    [
        "Grocery Store",
        "Supermarket Type1",
        "Supermarket Type2",
        "Supermarket Type3"
    ]
)

product_id_type = st.selectbox(
    "Product ID Type",
    ["FD", "NC", "DR"]
)

Store_Age_Years = st.number_input(
    "Store Age (Years)",
    min_value=0,
    value=10
)

Product_Type_Category = st.selectbox(
    "Product Type Category",
    ["Food", "Non-Consumable", "Drinks"]
)

# Create input dictionary
product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_Type": Product_Type,
    "Product_MRP": Product_MRP,
    "Store_Establishment_Year": Store_Establishment_Year,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "product_id_type": product_id_type,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

# Prediction
if st.button("Predict", type="primary"):

    response = requests.post(
        "https://bookish-space-halibut-wrwvqgx49wjf9jv9-7860.app.github.dev/v1/predict",
        json=product_data
    )

    if response.status_code == 200:

        result = response.json()
        predicted_sales = result["Sales"]

        st.success(
            f"Predicted Product Store Sales Total: ${predicted_sales:,.2f}"
        )

    else:

        st.error(
            f"Error in API request: {response.status_code}"
        )
        st.error(response.text)

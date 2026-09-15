import streamlit as st
import joblib
import pandas as pd

model = joblib.load("notebooks/models/olist_review_risk_model.pkl")

st.title("Olist Review Risk Predictor")

st.write(
    "Predict whether an order is likely to receive a bad review "
    "based on information available at the time of purchase."
)

st.header("Order Information")

estimated_delivery_days = st.number_input(
    "Estimated delivery days",
    min_value=0,
    value=12
)

item_count = st.number_input(
    "Number of items",
    min_value=1,
    value=1
)

total_price = st.number_input(
    "Total price (R$)",
    min_value=0.0,
    value=100.0
)

total_freight = st.number_input(
    "Freight cost (R$)",
    min_value=0.0,
    value=20.0
)

payment_count = st.number_input(
    "Number of payments",
    min_value=1,
    value=1
)

total_payment = st.number_input(
    "Total payment (R$)",
    min_value=0.0,
    value=120.0
)

max_installments = st.number_input(
    "Maximum installments",
    min_value=1,
    value=1
)

customer_state = st.selectbox(
    "Customer state",
    [
        "SP", "RJ", "MG", "RS", "PR", "SC", "BA",
        "DF", "ES", "GO", "PE", "CE", "PA", "MT",
        "MA", "MS", "PB", "RN", "AL", "PI", "SE",
        "RO", "TO", "AM", "AC", "AP", "RR"
    ]
)

purchase_month = st.slider(
    "Purchase month",
    min_value=1,
    max_value=12,
    value=6
)

purchase_dayofweek = st.slider(
    "Purchase day of week",
    min_value=0,
    max_value=6,
    value=2
)

purchase_hour = st.slider(
    "Purchase hour",
    min_value=0,
    max_value=23,
    value=12
)

if st.button("Predict Review Risk"):

    feature_columns = [
    "estimated_delivery_days",
    "item_count",
    "total_price",
    "total_freight",
    "payment_count",
    "total_payment",
    "max_installments",
    "purchase_month",
    "purchase_dayofweek",
    "purchase_hour",
    "customer_state_AL",
    "customer_state_AM",
    "customer_state_AP",
    "customer_state_BA",
    "customer_state_CE",
    "customer_state_DF",
    "customer_state_ES",
    "customer_state_GO",
    "customer_state_MA",
    "customer_state_MG",
    "customer_state_MS",
    "customer_state_MT",
    "customer_state_PA",
    "customer_state_PB",
    "customer_state_PE",
    "customer_state_PI",
    "customer_state_PR",
    "customer_state_RJ",
    "customer_state_RN",
    "customer_state_RO",
    "customer_state_RR",
    "customer_state_RS",
    "customer_state_SC",
    "customer_state_SE",
    "customer_state_SP",
    "customer_state_TO"
]

    input_data = pd.DataFrame(
    0,
    index=[0],
    columns=feature_columns
)

    input_data["estimated_delivery_days"] = estimated_delivery_days
    input_data["item_count"] = item_count
    input_data["total_price"] = total_price
    input_data["total_freight"] = total_freight
    input_data["payment_count"] = payment_count
    input_data["total_payment"] = total_payment
    input_data["max_installments"] = max_installments
    input_data["purchase_month"] = purchase_month
    input_data["purchase_dayofweek"] = purchase_dayofweek
    input_data["purchase_hour"] = purchase_hour

    state_column = f"customer_state_{customer_state}"

    if state_column in input_data.columns:
        input_data[state_column] = 1

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction")

    st.metric(
        "Bad Review Probability",
        f"{probability:.1%}"
    )

    if probability >= 0.17:
        st.error("HIGH RISK — This order is likely to receive a bad review.")
    else:
        st.success("LOW RISK — This order is less likely to receive a bad review.")
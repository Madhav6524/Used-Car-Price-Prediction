import pandas as pd
import streamlit as st
import joblib

df = pd.read_csv(
    "cardekho_imputated.csv"
)
df = df[df['selling_price'] < 3000000]
model_ann = joblib.load("ann_model.pkl")

st.title("Used Car Price Prediction")

st.sidebar.header("Car Selection")
brands = sorted(df['brand'].dropna().unique())
brand = st.sidebar.selectbox(
    "Brand",
    brands
)

df1 = df[df['brand'] == brand]
models = sorted(df1['model'].dropna().unique())
model = st.sidebar.selectbox(
    "Model",
    models
)

df2 = df1[df1['model'] == model]

st.sidebar.header("Car Specifications")

vehicle_age = st.sidebar.number_input(
    "Vehicle Age (Years)",
    min_value=1,
    max_value=30,
    value=int(df2['vehicle_age'].median())
)

if df2['max_power'].nunique() == 1:
    max_power = float(df2['max_power'].iloc[0])
    st.sidebar.write(f"Max Power: **{max_power} HP**")
else:
    max_power = st.sidebar.slider(
        "Max Power",
        min_value=float(df2['max_power'].min()),
        max_value=float(df2['max_power'].max()),
        value=float(df2['max_power'].median())
    )

if df2['engine'].nunique() == 1:
    engine = float(df2['engine'].iloc[0])
    st.sidebar.write(f"Engine: **{engine} CC**")
else:
    engine = st.sidebar.slider(
        "Engine",
        min_value=float(df2['engine'].min()),
        max_value=float(df2['engine'].max()),
        value=float(df2['engine'].median())
    )

if df2['mileage'].nunique() == 1:
    mileage = float(df2['mileage'].iloc[0])
    st.sidebar.write(f"Mileage: **{mileage} km/l**")
else:
    mileage = st.sidebar.slider(
        "Mileage",
        min_value=float(df2['mileage'].min()),
        max_value=float(df2['mileage'].max()),
        value=float(df2['mileage'].median())
    )

transmission_type = st.sidebar.selectbox(
    "Transmission",
    sorted(df2['transmission_type'].dropna().unique())
)

seats = st.sidebar.selectbox(
    "Seats",
    sorted(df2['seats'].dropna().unique())
)

fuel_type = st.sidebar.selectbox(
    "Fuel Type",
    sorted(df2['fuel_type'].dropna().unique())
)

km_driven = st.sidebar.number_input(
    "KM Driven",
    min_value=1,
    max_value=5000000,
    value=int(df2['km_driven'].median())
)

seller_type = st.sidebar.selectbox(
    "Seller Type",
    sorted(df2['seller_type'].dropna().unique())
)

st.subheader("Selected Car Information")

col1, col2, col3 = st.columns(3)

st.markdown("""
<style>
.card {
    padding: 10px 16px;
    margin: 5px 0;

    border-radius: 6px;
    border: 1px solid grey;
    
}
.card b {
    font-size: 16px;
}
.card span {
    float: right;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)


def card(name, value):
    st.markdown(
        f'<div class="card"><b>{name}</b><span>{value}</span></div>',
        unsafe_allow_html=True
    )


col1, col2, col3 = st.columns(3)

with col1:
    card("Brand", brand)
    card("Model", model)
    card("Vehicle Age", f"{vehicle_age} Years")
    card("KM Driven", f"{km_driven:,} km")

with col2:
    card("Max Power", f"{max_power:.2f} HP")
    card("Engine", f"{engine:.0f} CC")
    card("Mileage", f"{mileage:.2f} km/l")

with col3:
    card("Transmission", transmission_type)
    card("Fuel Type", fuel_type)
    card("Seats", seats)
    card("Seller Type", seller_type)

input_data = pd.DataFrame({
    'brand': [brand],
    'model': [model],
    'vehicle_age': [vehicle_age],
    'max_power': [max_power],
    'transmission_type': [transmission_type],
    'engine': [engine],
    'seats': [seats],
    'fuel_type': [fuel_type],
    'mileage': [mileage],
    'km_driven': [km_driven],
    'seller_type': [seller_type]
})

st.divider()

if st.button("Predict Price", use_container_width=True):
    prediction = model_ann.predict(input_data)
    st.subheader("Predicted Price")
    st.success(
        f"₹{prediction[0]:,.0f}"
    )
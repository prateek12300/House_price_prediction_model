import streamlit as st

st.title(" Real Estate Price & Rent Estimator")

city_rates_buy = {
    "Delhi": 10000,
    "Mumbai": 22000,
    "Pune": 8000,
    "Bangalore": 9500,
    "Hyderabad": 9000,
    "Chennai": 8500,
    "Kolkata": 7500,
    "Ahmedabad": 6500,
    "Jaipur": 6000,
    "Chandigarh": 11000
}

city_rates_rent = {
    "Delhi": 25,
    "Mumbai": 55,
    "Pune": 22,
    "Bangalore": 28,
    "Hyderabad": 26,
    "Chennai": 24,
    "Kolkata": 20,
    "Ahmedabad": 18,
    "Jaipur": 17,
    "Chandigarh": 27
}

city = st.selectbox("City", list(city_rates_buy.keys()))
mode = st.radio("Transaction Type", ["Buy", "Rent"])
bhk = st.slider("BHK", 1, 6, 2)
area = st.number_input("Area (sq ft)", 300, 5000, 1000)
floor = st.slider("Floor Number", 1, 50, 3)
age = st.slider("Age of Building (years)", 0, 40, 5)
furnish = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Fully Furnished"])
society = st.radio("Society Type", ["Normal", "Luxury"])

if st.button("Predict Price"):
    price = area * (city_rates_buy[city] if mode=="Buy" else city_rates_rent[city])

    price *= (1 + min((floor // 5) * 0.01, 0.05))
    price *= (1 - min(age * 0.007, 0.25))

    furnish_factor = {
        "Unfurnished": 1.00,
        "Semi-Furnished": 1.07,
        "Fully Furnished": 1.15
    }[furnish]

    price *= furnish_factor
    price *= (1.25 if society=="Luxury" else 1.00)

    if mode=="Buy":
        st.success(f"Estimated Property Price: ₹{price:,.0f}")
    else:
        st.success(f"Estimated Monthly Rent: ₹{price:,.0f}")

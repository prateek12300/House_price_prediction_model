import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data.csv")

# Features & target
X = df[['bhk', 'area', 'city']]
y = df['price']

# Convert city → numeric
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), ['city'])],
    remainder='passthrough'
)

# Build pipeline
model = Pipeline(steps=[
    ('transformer', ct),
    ('regressor', LinearRegression())
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "house_price_model.pkl")

print("🎉 Model trained & saved as house_price_model.pkl")

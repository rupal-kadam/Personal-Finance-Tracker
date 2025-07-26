import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Raw data
data = {
    "Make": ["Honda", "Honda", "Toyota", "Nissan", "Toyota", "Honda", "Ford", "Chevrolet", "Chevrolet", "Dodge", "Dodge"],
    "Model": ["Accord", "Accord", "Camry", "Altima", "Corolla", "Civic", "F-150", "Silverado", "Impala", "Charger", "Charger"],
    "Color": ["Red", "Blue", "Black", "Green", "Black", "White", "Black", "Green", "Silver", "Silver", "Silver"],
    "Mileage": ["63,512", "95,135", "75,006", "69,847", "87,278", "1,38,789", "89,073", "1,09,231", "87,675", "34,853", "58,173"],
    "Sell_Price": [4000, 2500, 4500, 3826, 2224, 2723, 3950, 4959, 3791, 4349, 4252]
}

# Create DataFrame
df = pd.DataFrame(data)

# Clean "Mileage" column (remove commas and convert to int)
df["Mileage"] = df["Mileage"].str.replace(",", "").astype(int)

# Standardization (Z-score)
scaler_std = StandardScaler()
df["Mileage_Standardized"] = scaler_std.fit_transform(df[["Mileage"]])
df["Sell_Price_Standardized"] = scaler_std.fit_transform(df[["Sell_Price"]])

# Normalization (Min-Max)
scaler_norm = MinMaxScaler()
df["Mileage_Normalized"] = scaler_norm.fit_transform(df[["Mileage"]])
df["Sell_Price_Normalized"] = scaler_norm.fit_transform(df[["Sell_Price"]])

# Output result
df_scaled = df[["Make", "Model", "Color", "Mileage", "Sell_Price",
                "Mileage_Standardized", "Sell_Price_Standardized",
                "Mileage_Normalized", "Sell_Price_Normalized"]]

df_scaled.round(2)

import numpy as np
import pickle
import streamlit as st

# Load trained model
loaded_model = pickle.load(open('weather.sav', 'rb'))

def weather_prediction(input_data):
    input_data_as_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'Rainy'
    elif prediction[0] == 0:
        return 'Cloudy'
    elif prediction[0] == 3:
        return 'Sunny'
    else:
        return 'Snowy'

def main():
    st.title("🌦️ Weather Data Prediction App")

    # Numerical input fields
    temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, step=0.1)
    precipitation = st.number_input("Precipitation (%)", min_value=0.0, max_value=100.0, step=0.1)
    pressure = st.number_input("Atmospheric Pressure (hPa)", min_value=800.0, max_value=1100.0, step=0.1)
    uv_index = st.number_input("UV Index", min_value=0.0, max_value=15.0, step=0.1)
    visibility = st.number_input("Visibility (km)", min_value=0.0, max_value=50.0, step=0.1)

    # Dropdowns for categorical values
    cloud_cover = st.selectbox("Cloud Cover", [
        "0 - Overcast", 
        "1 - Partly Cloudy", 
        "2 - Clear", 
        "3 - Cloudy"
    ])

    season_val = st.selectbox("Season", [
        "0 - Winter", 
        "1 - Spring", 
        "2 - Autumn", 
        "3 - Summer"
    ])

    location_val = st.selectbox("Location", [
        "0 - Inland", 
        "1 - Mountain", 
        "2 - Coastal"
    ])

    if st.button("🔍 Predict Weather"):
        try:
            # Extract only the numeric value from dropdowns
            input_list = [
                temperature,
                humidity,
                wind_speed,
                precipitation,
                float(cloud_cover.split(" - ")[0]),
                pressure,
                uv_index,
                float(season_val.split(" - ")[0]),
                visibility,
                float(location_val.split(" - ")[0])
            ]
            prediction = weather_prediction(input_list)
            st.success(f"🌤️ Predicted Weather: **{prediction}**")

        except Exception as e:
            st.error(f"❗ Error occurred: {str(e)}")
if __name__ == '__main__':
    main()

import streamlit as st
import requests
import os
from openai import OpenAI, OpenAIError

WEATHER_API_KEY = "e7675ba689af4a24a71104124250109"  
OPENAI_API_KEY = "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"

BASE_URL = "https://api.weatherapi.com/v1/current.json"
client = OpenAI(api_key=OPENAI_API_KEY)
st.title("🌤️ Weather Now App (Automatic Location)")

try:
    ip_data = requests.get("https://ipinfo.io/json").json()
    city = ip_data.get("city")
    region = ip_data.get("region")
    country = ip_data.get("country")
except:
    st.warning("Could not detect location automatically. Please enter manually.")
    city = st.text_input("Enter city name")

if city:
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "error" in data:
        st.error(f"Error: {data['error']['message']}")
    else:
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        icon = data["current"]["condition"]["icon"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]

        st.success(f"📍 {location}, {country}")
        st.metric("🌡 Temperature (°C)", temp)
        st.write(f"**Condition:** {condition}")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"💨 Wind Speed: {wind_kph} kph")
        st.image("https:" + icon, width=100)

        prompt = (
            f"The current weather in {location}, {country} is {temp}°C with {condition}, "
            f"humidity {humidity}%, wind speed {wind_kph} kph. "
            f"Write a short, friendly summary and give suggestions for what people should do or wear."
        )

        try:
            with st.spinner("Generating AI weather summary..."):
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful weather assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150,
                    temperature=0.7
                )
                summary = completion.choices[0].message.content

        except OpenAIError:
            summary = "🤖 AI summary not available (quota exceeded)."

        st.subheader("AI Weather Assistant Says:")
        st.write(summary)

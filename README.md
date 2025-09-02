# Weather_now_app
Weather Now is a real-time web application that automatically detects your location and shows the current weather conditions. It also provides an AI-generated friendly summary with suggestions on what to do or wear based on the weather. 
Features
Automatic Location Detection – Detects the user’s city automatically using IP-based geolocation.
Real-Time Weather Data – Shows temperature, weather condition, humidity, and wind speed.
Weather Icons – Displays a relevant weather icon for easy visualization.
AI Weather Summary – Uses OpenAI GPT-4 or GPT-3.5 (fallback) to give a short friendly weather summary and advice.
Graceful Fallback – If OpenAI API quota is exceeded, the app still works with full weather information.

Python Libraries: streamlit, requests, openai

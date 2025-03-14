# Import Libraries
import requests
import pandas as pd
from datetime import datetime


# Import really bad dad joke (https://jokeapi.dev/)
response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
if response.status_code == 200:
    joke_data = response.json()
    joke = joke_data.get("joke", "Potato!")
else:
    joke = "Computer says no..."


# Create a DataFrame with the joke and export date
joke_df = pd.DataFrame({
    "Joke": [joke],
    "Export Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
})


# Export Data
joke_df.to_csv("_data/joke.csv", index=False)

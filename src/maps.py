import pandas as pd
import plotly.express as px
import requests
from helpers.config import get_settings
from concurrent.futures import ThreadPoolExecutor, as_completed

app_settings = get_settings()
# Mapbox
mapbox_access_token = app_settings.MAPBOX_ACCESS_TOKEN

# API Setup
locationiq_api_key = app_settings.LOCATIONIQ_API_KEY
ENDPOINT = 'https://us1.locationiq.com/v1/search.php'

# Cache File
cache_path = app_settings.CACHE_PATH
try:
    cache_df = pd.read_csv(cache_path, index_col='Place')
except FileNotFoundError:
    cache_df = pd.DataFrame(columns=['Place', 'Latitude', 'Longitude']).set_index('Place')


def geocode_location(place):
    if place in cache_df.index:
        # Fetch from cache
        location = cache_df.loc[place]
        lat, lon = location['Latitude'], location['Longitude']
    else:
        params = {
            'key': locationiq_api_key,
            'q': place,
            'format': 'json'
        }
        response = requests.get(ENDPOINT, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                lat, lon = float(data[0]['lat']), float(data[0]['lon'])
                # Save to cache
                cache_df.loc[place] = [lat, lon]
                cache_df.to_csv(cache_path)
            else:
                lat, lon = (None, None)
        else:
            lat, lon = (None, None)

    return lat, lon


def geocode(places: pd.Series) -> tuple[list, list]:
    print(f"Places Before Clearing: {len(places)}")
    places = places.unique()
    print(f"Places After Clearing: {len(places)}")

    results = [[], []]
    with ThreadPoolExecutor(
            max_workers=3) as executor:  # To Speed up Geocoding. There will be some missing values but better than slow :)
        # Create a future for each geocoding request
        futures = {executor.submit(geocode_location, place): place for place in places}
        for future in as_completed(futures):
            lat, lon = future.result()
            results[0].append(lat)
            results[1].append(lon)
    return results


def generate_heatmap(matched_jobs):
    locations = matched_jobs['job_location']
    latitudes, longitudes = geocode(locations)
    df = pd.DataFrame({
        'latitude': latitudes,
        'longitude': longitudes,
    })
    # Making a Heatmap using mapbox website
    heatmap = px.density_mapbox(df, lat="latitude", lon="longitude", zoom=1, height=600, radius=20)
    heatmap.update_layout(
        mapbox_style="mapbox://styles/osama-ashraf/clvxxlnsh01vt01o03r6dfca8",  # ? My Specific Style 😎😎
        mapbox_accesstoken=mapbox_access_token,
        mapbox={
            'center': {'lat': 0, 'lon': 0},  # Centering at the geometric center of the world map
        },
        margin={'t': 0, 'r': 0, 'b': 0, 'l': 0}
    )

    print("Generating Heatmap has finished !")

    return heatmap


if __name__ == "__main__":
    S = pd.Series(
        ['Egypt', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'United Kingdom',
         'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'USA', 'United Kingdom', 'USA',
         'United Kingdom', 'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'USA', 'United Kingdom',
         'USA', 'United Kingdom', 'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'USA',
         'United Kingdom', 'USA', 'United Kingdom', 'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA',
         'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom',
         'USA', 'USA', 'United Kingdom', 'USA', 'United Kingdom', 'USA'])

    x, y = geocode(S)

    print(x, y)

# Tourist Map Generator

## Overview
This Python script uses the Google Maps API to generate a tourist map with attraction places. It can optionally group attractions based on proximity using marker clustering.

## Dependencies
Ensure you have the following Python libraries installed:

```bash
pip install requests geopy folium
```

## Usage

1. **Obtain Google Maps API Key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the Google Maps Geocoding API.
   - Generate an API key and save it in a file named `api.txt` in the script's directory.

2. **Prepare Attractions List:**
   - Create a text file named `attractions.txt` containing the list of attraction places, each on a new line.

3. **Optional: Specify City for Improved Geocoding:**
   - If you have additional information about the city where attractions are located, you can provide it in a file named `city.txt` in the script's directory.

4. **Run the Script:**
   - Execute the script by running the following command in your terminal:

     ```bash
     python map.py
     ```


5. **View the Map:**
   - After the script completes, it will generate an HTML file containing the tourist map.
   - Open the generated HTML file in your web browser to view the map.

## Additional Options

- **Enable Clustering:**
  - By default, clustering is disabled. If you want to enable marker clustering for proximity grouping, set `enable_clustering=True` in the `create_map` function.

- **Customizing Marker Colors:**
  - You can customize the marker colors in the script by modifying the `folium.Icon(color=...)` parameter.

## File Structure

- `map.py`: Your main Python script.
- `api.txt`: File containing your Google Maps API key.
- `attractions.txt`: File containing the list of attraction places.
- `city.txt`: Optional file specifying the city for improved geocoding.
- Generated HTML files: Tourist maps created by the script.
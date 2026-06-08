# WildPath

WildPath is a Flask web app that helps people explore Seattle-area bird observations using public iNaturalist data.

## Features

- Choose one of eight birds: Snow Goose, Bald Eagle, Great Blue Heron, Canada Goose, Mallard, Osprey, Anna's Hummingbird, American Crow
- Choose a region: Seattle, Puget Sound, or Western Washington
- Optional year and month filters
- Live iNaturalist public observations API request
- Leaflet map with observation points
- Summary panel with observation count, mapped points, date range, and most common month
- Recent observation cards with photos, dates, locations, and links
- How it works page

## API key

No API key is required. This app only reads public iNaturalist observation data and does not write data or access private user information.

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --debug run
```

Open http://127.0.0.1:5000/ in a browser.

## Data note

iNaturalist observations are community-submitted sightings. WildPath does not show GPS tracking paths of individual birds.

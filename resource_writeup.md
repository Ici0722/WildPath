# Resource Write-up: iNaturalist API

WildPath uses the iNaturalist public observations API. The app sends GET requests to the observations endpoint with parameters such as taxon ID, latitude, longitude, radius, year/date range, and month. The API returns JSON data, including observation dates, coordinates, place guesses, taxon names, photos, and links to the original iNaturalist observation.

For this project, I use public observation data only, so no API key is required. I do not create, update, or delete observations, and I do not access private user information. The app is designed around small interactive searches rather than bulk downloading.

The main limitation is that iNaturalist observations are community submitted sightings. They show where people reported seeing birds, not GPS tracking paths of individual birds. This changed my project from an animal migration path visualizer into a Seattle bird observation explorer.

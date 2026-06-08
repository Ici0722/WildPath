# 1–2 Minute Demo Script

Hi, this is WildPath, a Seattle bird finder that helps people explore public bird observations around Seattle and the Pacific Northwest.

My original idea was to show individual animal migration paths, but I learned that tracking data from Movebank often requires study permissions or login access. I changed the project to use iNaturalist public observations instead, which is more reliable for a public Flask app.

On the Explore page, users can choose one of eight common or recognizable birds, such as Mallard, Bald Eagle, Snow Goose, or Anna's Hummingbird. They can choose Seattle, Puget Sound, or Western Washington, and optionally filter by year and month.

When I click Find bird, the Flask app sends a live request to the iNaturalist API. The Python code parses the returned JSON into observation objects. The map shows the observation points using Leaflet, and the summary panel shows the total observations, mapped points, date range, and most common month.

Below the map, recent observation cards show photos, dates, locations, and links to the original iNaturalist observations.

The part I am most proud of is turning a complicated public dataset into an interface that feels easier for everyday bird-curious people to explore.

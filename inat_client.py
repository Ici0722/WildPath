"""Functions for requesting public observation data from iNaturalist."""

import json
import urllib.error
import urllib.parse
import urllib.request
from models import Observation

BASE_URL = "https://api.inaturalist.org/v1/observations"

def safe_get_json(base_url, args):
    """Safely request JSON data from a web API using urllib."""
    url = base_url + "?" + urllib.parse.urlencode(args)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "WildPath HCDE310 student project (public observation viewer)",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as error:
        print("Error from iNaturalist server:", error.code)
        return None
    except urllib.error.URLError as error:
        print("Failed to reach iNaturalist:", error.reason)
        return None
    except json.JSONDecodeError as error:
        print("Could not parse JSON:", error)
        return None


def build_date_args(year, month):
    """Build date filters for iNaturalist API from year and optional month."""
    args = {}
    if year != "":
        if month != "":
            month_number = int(month)
            start_date = "{}-{:02d}-01".format(year, month_number)
            if month_number == 12:
                end_date = "{}-12-31".format(year)
            else:
                end_date = "{}-{:02d}-01".format(year, month_number + 1)
            args["d1"] = start_date
            args["d2"] = end_date
        else:
            args["d1"] = "{}-01-01".format(year)
            args["d2"] = "{}-12-31".format(year)
    elif month != "":
        args["month"] = month
    return args


def fetch_observations(bird, region, year, month, per_page=80):
    """Fetch public bird observations from iNaturalist.

    The API request is based on user choices from the Flask form. The returned
    dictionaries are converted into Observation objects for easier use in the
    rest of the app.
    """
    args = {
        "taxon_id": bird["taxon_id"],
        "lat": region["lat"],
        "lng": region["lng"],
        "radius": region["radius_km"],
        "quality_grade": "research,needs_id",
        "geo": "true",
        # "photos": "true",
        "order_by": "observed_on",
        "order": "desc",
        "per_page": per_page,
    }

    date_args = build_date_args(year, month)
    for key in date_args:
        args[key] = date_args[key]
    print(args)
    data = safe_get_json(BASE_URL, args)
    print("total_results:", data.get("total_results") if data else "no data")
    if data is None:
        return [], 0, "Could not retrieve data from iNaturalist. Please try again later."

    raw_results = data.get("results", [])
    observations = []
    for item in raw_results:
        obs = Observation(item)
        observations.append(obs)

    total_results = data.get("total_results", len(observations))
    return observations, total_results, ""

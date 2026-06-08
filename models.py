"""Small data classes and summary helpers for WildPath."""

from collections import Counter
from datetime import datetime

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December",
}


class Observation:
    """Represents one iNaturalist observation shown in the app."""

    def __init__(self, raw_data):
        self.id = raw_data.get("id")
        self.observed_on = raw_data.get("observed_on") or "Unknown date"
        self.uri = raw_data.get("uri") or "https://www.inaturalist.org"

        taxon = raw_data.get("taxon") or {}
        self.common_name = taxon.get("preferred_common_name") or taxon.get("name") or "Unknown bird"
        self.scientific_name = taxon.get("name") or ""

        place_guess = raw_data.get("place_guess") or "Location not listed"
        self.place_guess = place_guess

        geojson = raw_data.get("geojson") or {}
        coords = geojson.get("coordinates") or []
        self.longitude = None
        self.latitude = None
        if len(coords) == 2:
            self.longitude = coords[0]
            self.latitude = coords[1]

        photos = raw_data.get("photos") or []
        self.photo_url = ""
        if len(photos) > 0:
            photo_data = photos[0]
            self.photo_url = photo_data.get("url") or ""
            # iNaturalist often returns square thumbnails. Medium looks nicer in cards.
            self.photo_url = self.photo_url.replace("square", "medium")

    def has_location(self):
        return self.latitude is not None and self.longitude is not None

    def month_number(self):
        try:
            return datetime.strptime(self.observed_on, "%Y-%m-%d").month
        except ValueError:
            return None

    def date_for_display(self):
        try:
            parsed_date = datetime.strptime(self.observed_on, "%Y-%m-%d")
            return parsed_date.strftime("%b %-d, %Y")
        except ValueError:
            return self.observed_on

    def to_map_dict(self):
        return {
            "id": self.id,
            "common_name": self.common_name,
            "scientific_name": self.scientific_name,
            "observed_on": self.date_for_display(),
            "place_guess": self.place_guess,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "photo_url": self.photo_url,
            "uri": self.uri,
        }


def most_common_month(observations):
    """Returns the most common observation month name, or 'No data'."""
    month_numbers = []
    for obs in observations:
        month = obs.month_number()
        if month is not None:
            month_numbers.append(month)

    if len(month_numbers) == 0:
        return "No data"

    month_counter = Counter(month_numbers)
    most_common_number = month_counter.most_common(1)[0][0]
    return MONTH_NAMES[most_common_number]


def date_range_text(observations):
    """Returns the date range for returned observations."""
    dates = []
    for obs in observations:
        try:
            dates.append(datetime.strptime(obs.observed_on, "%Y-%m-%d"))
        except ValueError:
            pass

    if len(dates) == 0:
        return "No dates"

    first_date = min(dates).strftime("%b %-d, %Y")
    last_date = max(dates).strftime("%b %-d, %Y")
    if first_date == last_date:
        return first_date
    return "{} – {}".format(first_date, last_date)


def make_summary(observations, total_results):
    """Builds the summary panel shown next to the map."""
    mapped_points = 0
    for obs in observations:
        if obs.has_location():
            mapped_points = mapped_points + 1

    return {
        "total_results": total_results,
        "returned_observations": len(observations),
        "mapped_points": mapped_points,
        "common_month": most_common_month(observations),
        "date_range": date_range_text(observations),
    }

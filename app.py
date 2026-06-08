"""WildPath Flask app.

A public iNaturalist observation explorer for eight Seattle-area birds.
"""

from flask import Flask, render_template, request

from config import (
    BIRDS,
    DEFAULT_BIRD_KEY,
    DEFAULT_MONTH,
    DEFAULT_REGION_KEY,
    DEFAULT_YEAR,
    MONTHS,
    REGIONS,
    YEARS,
)
from inat_client import fetch_observations
from models import make_summary

app = Flask(__name__)

BIRD_CARD_IMAGES = {
    "snow-goose": "img/snow-goose.jpg",
    "bald-eagle": "img/bald-eagle.jpg",
    "great-blue-heron": "img/great-blue-heron.jpg",
    "canada-goose": "img/canada-goose.jpg",
    "mallard": "img/mallard.jpg",
    "osprey": "img/osprey.jpg",
    "annas-hummingbird": "img/annas-hummingbird.jpg",
    "american-crow": "img/american-crow.jpg",
}


def find_by_key(items, key, fallback_key):
    """Finds a dictionary in a list by its key value."""
    for item in items:
        if item["key"] == key:
            return item

    for item in items:
        if item["key"] == fallback_key:
            return item

    return items[0]


@app.route("/")
def explore():
    selected_bird_key = request.args.get("bird", DEFAULT_BIRD_KEY)
    selected_region_key = request.args.get("region", DEFAULT_REGION_KEY)
    selected_year = request.args.get("year", DEFAULT_YEAR)
    selected_month = request.args.get("month", DEFAULT_MONTH)

    selected_bird = find_by_key(BIRDS, selected_bird_key, DEFAULT_BIRD_KEY)
    selected_region = find_by_key(REGIONS, selected_region_key, DEFAULT_REGION_KEY)

    observations, total_results, error_message = fetch_observations(
        selected_bird,
        selected_region,
        selected_year,
        selected_month,
    )

    summary = make_summary(observations, total_results)

    map_points = []
    for observation in observations:
        if observation.has_location():
            map_points.append(observation.to_map_dict())

    recent_observations = observations[:8]

    bird_cards = []
    for bird in BIRDS:
        bird_copy = bird.copy()
        bird_copy["photo_file"] = BIRD_CARD_IMAGES.get(bird["key"], "")
        bird_cards.append(bird_copy)
    
    selected_bird_photo = "img/{}.jpg".format(selected_bird["key"])

    return render_template(
        "explore.html",
        page="explore",
        birds=BIRDS,
        bird_cards=bird_cards,
        regions=REGIONS,
        months=MONTHS,
        years=YEARS,
        selected_bird=selected_bird,
        selected_bird_photo=selected_bird_photo,
        selected_region=selected_region,
        selected_year=selected_year,
        selected_month=selected_month,
        observations=recent_observations,
        map_points=map_points,
        summary=summary,
        error_message=error_message,
    )


@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html", page="how")


if __name__ == "__main__":
    app.run(debug=True)
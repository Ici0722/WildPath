"""Configuration data for WildPath.

The user-facing bird names are mapped to iNaturalist taxon IDs so users do not
need to know technical API parameters.
"""

BIRDS = [
    {
        "key": "snow-goose",
        "name": "Snow Goose",
        "scientific": "Anser caerulescens",
        "taxon_id": 558426,
        "taxon_name": "Anser caerulescens",
    },
    {
        "key": "bald-eagle",
        "name": "Bald Eagle",
        "scientific": "Haliaeetus leucocephalus",
        "taxon_id": 5305,
        "taxon_name": "Haliaeetus leucocephalus",
    },
    {
        "key": "great-blue-heron",
        "name": "Great Blue Heron",
        "scientific": "Ardea herodias",
        "taxon_id": 4956,
        "taxon_name": "Ardea herodias",
    },
    {
        "key": "canada-goose",
        "name": "Canada Goose",
        "scientific": "Branta canadensis",
        "taxon_id": 6921,
        "taxon_name": "Branta canadensis",
    },
    {
        "key": "mallard",
        "name": "Mallard",
        "scientific": "Anas platyrhynchos",
        "taxon_id": 6930,
        "taxon_name": "Anas platyrhynchos",
    },
    {
        "key": "osprey",
        "name": "Osprey",
        "scientific": "Pandion haliaetus",
        "taxon_id": 116999,
        "taxon_name": "Pandion haliaetus",
    },
    {
        "key": "annas-hummingbird",
        "name": "Anna's Hummingbird",
        "scientific": "Calypte anna",
        "taxon_id": 5562,
        "taxon_name": "Calypte anna",
    },
    {
        "key": "american-crow",
        "name": "American Crow",
        "scientific": "Corvus brachyrhynchos",
        "taxon_id": 4755,
        "taxon_name": "Corvus brachyrhynchos",
    },
]

REGIONS = [
    {
    "key": "all-regions",
    "name": "All regions",
    "description": "Seattle, Puget Sound and Western Washington",
    "lat": 47.6,
    "lng": -122.4,
    "radius_km": 250,
    "zoom": 7,
    },
    {
        "key": "seattle",
        "name": "Seattle",
        "description": "Seattle city area",
        "lat": 47.6062,
        "lng": -122.3321,
        "radius_km": 35,
        "zoom": 10,
    },
    {
        "key": "puget-sound",
        "name": "Puget Sound",
        "description": "Greater Puget Sound area",
        "lat": 47.65,
        "lng": -122.45,
        "radius_km": 65,
        "zoom": 9,
    },
    {
        "key": "western-washington",
        "name": "Western Washington",
        "description": "Western Washington bird observations",
        "lat": 47.5,
        "lng": -122.4,
        "radius_km": 160,
        "zoom": 7,
    },
]

MONTHS = [
    {"value": "", "name": "All months"},
    {"value": "1", "name": "January"},
    {"value": "2", "name": "February"},
    {"value": "3", "name": "March"},
    {"value": "4", "name": "April"},
    {"value": "5", "name": "May"},
    {"value": "6", "name": "June"},
    {"value": "7", "name": "July"},
    {"value": "8", "name": "August"},
    {"value": "9", "name": "September"},
    {"value": "10", "name": "October"},
    {"value": "11", "name": "November"},
    {"value": "12", "name": "December"},
]

YEARS = ["", "2026", "2025", "2024", "2023", "2022", "2021", "2020"]

DEFAULT_BIRD_KEY = "snow-goose"
DEFAULT_REGION_KEY = "seattle"
DEFAULT_YEAR = ""
DEFAULT_MONTH = ""

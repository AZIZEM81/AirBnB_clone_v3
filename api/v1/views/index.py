#!/usr/bin/python3
"""Index view for the API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each objects by type"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    stats = {}
    for key, value in classes.items():
        stats[key] = storage.count(value)
    return jsonify(stats)

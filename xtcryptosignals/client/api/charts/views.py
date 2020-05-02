__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    current_app,
)


bp = Blueprint("charts", __name__)


@bp.route("/charts/cfgi/BTC/<frequency>", methods=["GET"])
def cfgi_btc(frequency):
    response = requests.get(
        url="{}charts/cfgi/BTC/{}".format(
            current_app.config["SERVER_API_BASE_URL"], frequency
        ),
    )
    return response.json(), response.status_code


@bp.route("/charts/<coin_or_token>/<frequency>", methods=["GET"])
def coin_or_token_frequency(coin_or_token, frequency):
    response = requests.get(
        url="{}charts/{}/{}".format(
            current_app.config["SERVER_API_BASE_URL"], coin_or_token, frequency
        ),
    )
    return response.json(), response.status_code


@bp.route("/charts/tether/<coin_or_token>/<frequency>", methods=["GET"])
def tether_btc(coin_or_token, frequency):
    response = requests.get(
        url="{}charts/tether/{}/{}".format(
            current_app.config["SERVER_API_BASE_URL"], coin_or_token, frequency
        ),
    )
    return response.json(), response.status_code


@bp.route("/charts/twitter", methods=["GET"])
def twitter():
    response = requests.get(
        url="{}charts/twitter".format(
            current_app.config["SERVER_API_BASE_URL"]
        ),
    )
    return response.json(), response.status_code

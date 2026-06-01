import time
import hmac
import hashlib
from urllib import response
import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL")


class BinanceClient:

    def __init__(self):
        self.api_key = API_KEY
        self.secret_key = SECRET_KEY
        self.base_url = BASE_URL

    def generate_signature(self, params):

        query_string = urlencode(params)

        signature = hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        endpoint = "/fapi/v1/order"

        url = self.base_url + endpoint

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        if order_type.upper() == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        signature = self.generate_signature(params)

        params["signature"] = signature

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(
            url,
            headers=headers,
            params=params
        )

        response.raise_for_status()
        return response.json()
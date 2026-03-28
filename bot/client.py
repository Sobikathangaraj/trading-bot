import time
import hmac
import hashlib
import requests
from bot.logging_config import setup_logger

logger = setup_logger()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _sign(self, params: dict) -> dict:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        signature = hmac.new(
            self.api_secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, **params) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 60000
        params = self._sign(params)
        logger.info(f"Sending order: {params}")

        try:
            response = self.session.post(
                f"{BASE_URL}/fapi/v1/order",
                params=params
            )
            data = response.json()
            logger.info(f"Response: {data}")

            if "code" in data and data["code"] != 200:
                logger.error(f"API Error: {data}")
                raise Exception(f"API Error {data['code']}: {data['msg']}")

            return data

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise
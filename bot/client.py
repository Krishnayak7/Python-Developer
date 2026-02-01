import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **kwargs):
        try:
            logger.info(f"API Request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"API Response: {response}")
            return response
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Binance Error: {e}")
            raise
        except Exception as e:
            logger.exception("Unexpected error")
            raise

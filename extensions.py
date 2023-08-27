import requests
import json
from config import keys
class ConvertionExcepyion(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExcepyion(f'Невозможно перевести одинаковые валюты: {base}.')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionExcepyion(f'Не удалось обработать валюту: {quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionExcepyion(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExcepyion(f'Не удалось обработать количество: {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount
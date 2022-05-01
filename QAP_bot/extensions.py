import requests
import json
from config import keys


class APIException (Exception):
    pass

class MoneyConverter:
    @staticmethod
    def get_price(base:str,quote:str,amount:str):

        if base == quote:
            raise APIException (f'Невозможно перевести одинаковые валюты {quote}.')

        try:
            {keys[quote]}
        except KeyError:
            raise APIException (f'Не удается обработать валюту {quote}.')

        try:
            {keys[base]}
        except KeyError:
            raise APIException (f'Не удается обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удается обработать количество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[base]}&tsyms={keys[quote]}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base


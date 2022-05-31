from operator import methodcaller
import requests
from config.api import *
from config.colors import *

class Route:
    def get(endpoint: str, controller: methodcaller or function, params: dict):
        try:
            response = requests.get(API_URL + endpoint, params=params)
            if response.status_code != 200:
                print(f"{color.WARNING}[{response.status_code}] {response.json()['message']}{color.ENDC}")
            else:
                controller(response)
        except Exception as err:
            print(err)
            print(f"{color.FAIL}Upps something went wrong{color.ENDC}")

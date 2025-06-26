import requests

import configuration

def authentication(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json = user_body)

def create_kit(header, kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json = kit_body, headers = header)

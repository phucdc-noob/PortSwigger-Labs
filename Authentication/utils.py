import requests
from concurrent.futures import ThreadPoolExecutor

def send_request(url, headers = None, data = None, json = None):
    return requests.post(url, headers=headers, data=data, json=json)

def multi_request(urls):
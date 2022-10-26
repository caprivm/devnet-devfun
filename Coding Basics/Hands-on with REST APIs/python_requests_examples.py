"""import requests
import json

url = "http://localhost:8080/v1/books"
books = requests.get(url)

# print(json.dumps(books.json(), indent=4))

book = {
  "name": "The Art of Computer Programming",
  "authors": ["Donald Knuth"],
  "date": 1968,
  "isbn": "0-201-03801-3"
}

response = requests.post(url, json=book)
print(response.status_code)
"""

"""
import requests
import json
url = "http://localhost:8080/v1/books"
book = {
    "name": "The Art of Computer Programming",
    "authors": [
    "Donald Nuth"       # Typo
    ],
    "date": 1968,
    "isbn": "0-201-03801-3"
}

# Add the Book with a Typo to the author's name
response = requests.post(url, json=book)
book_data = response.json()

print("Response after ADDING the book to the library")
print(json.dumps(book_data, indent=4))


# Let's now update the Book with the correct author's name.
book_data["authors"] = ["Donald Knuth"]
update_book_url = "http://localhost:8080/v1/books/{}".format(book_data['uuid'])
response = requests.put(update_book_url, json=book_data)

print("http status code after updating the book: ", response.status_code)
"""

"""
import requests
import json
url = "http://localhost:8080/v1/books"
book = {
    "name": "The Art of Computer Programming",
    "authors": [
    "Donald Knuth"
    ],
    "date": 1968,
    "isbn": "0-201-03801-3"
}

# Add the Book
response = requests.post(url, json=book)
book_data = response.json()


# Let's now delete the book that we just added to the library.
delete_book_url = "http://localhost:8080/v1/books/{}".format(book_data['uuid'])
response = requests.delete(delete_book_url)

print("http status code after deleting the book: ", response.status_code)
"""


import requests
from requests.auth import HTTPBasicAuth
import json
import sys
# Here we will attempt to retrieve all user accounts from the library
# Since user accounts are considered a protected resource, only those who have
# admin credentials should be able to access it.
url = "http://localhost:8080/v1/accounts"

## This is unsafe as the username and password are stored in plain text
username = 'admin'
password = 'w0FimhVrty1ck9Pf2UAK4luOnkEgrDvy1VEK9iZsZOk='

# Leverage the HTTPBasicAuth class provided by the requests package
accounts = requests.get(url, auth=HTTPBasicAuth(username, password))
try:
    accounts.raise_for_status()
except requests.exceptions.HTTPError as e:
    # this code will not be executed if the username and password are correct!
    print("Error: {}".format(e))
    sys.exit()
# This code will be executed
print(accounts.status_code)

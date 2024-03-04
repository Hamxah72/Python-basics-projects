import requests
import pprint as pp
r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")

q = r.status_code
print(q)
w = r.text
print(w)
print(type(w))

import json
question = json.loads(r.text)
print(question)
print(type(question))

pp.pp(question)
question["results"][0]["category"]



# k = r.status_code
# print(k)
# y = r.headers
# print(y)
# z = r.headers["Date"]
# print(z)
# m = r.text
# print(m)

# API = Application Programming Interface

# JSON = Java Script Object Notation


import requests 

# virtualenv
print("requests version: " + requests.__version__)

# curl
res = requests.get("http://www.google.com")
print(res.text)
import requests 

# virtualenv
print("requests version: " + requests.__version__)

# curl
res = requests.get("https://raw.githubusercontent.com/signed-long/404-lab1/main/lab1.py")
print(res.text)
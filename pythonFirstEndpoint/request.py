import requests

dataJson = {
      "table": "",
      "keys": [],
      "data": []
    }

requestHeaders = {  "Content-Type": "application/json", 
                    "Cookie":""}

requestUrl = "https://";                                                                                                                                                                                                                                                                                                                                   

response = requests.post(requestUrl,
    json=dataJson,
    headers= requestHeaders,
    verify = False
)

print(response.json())
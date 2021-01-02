import http.client

conn = http.client.HTTPSConnection("securities-end-of-day-trading-data.p.rapidapi.com")

headers = {
    'accept-language': "he-IL",
    'x-rapidapi-key': "f1454ed893msh2d4e8acf6f46075p1e3f71jsn7fcf994b62f4",
    'x-rapidapi-host': "securities-end-of-day-trading-data.p.rapidapi.com"
    }

conn.request("GET", "/securities/end-of-day-trading-data/2020/3/16?securityId=1159029", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

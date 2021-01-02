import http.client

conn = http.client.HTTPSConnection("quotes-end-of-day.p.rapidapi.com")

headers = {
    'accept-language': "he-IL",
    'x-rapidapi-key': "f1454ed893msh2d4e8acf6f46075p1e3f71jsn7fcf994b62f4",
    'x-rapidapi-host': "quotes-end-of-day.p.rapidapi.com"
    }

conn.request("GET", "/securities/quotes-end-of-day/1159029/2020/10/19?offset=0&limit=50", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

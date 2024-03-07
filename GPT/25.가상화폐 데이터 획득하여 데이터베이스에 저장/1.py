import requests
import json

def coins(current):
    url = "https://www.upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC"
    querystring = {"isDetails":"true"}
    response = requests.request("GET",url,params=querystring)
    response_json = json.loads(response.text)
    KRWticker = []
    BTCticker = []
    USDTticker = []
    for a in response_json:
        if "KRW-" in a["market"]:
            KRWticker.append(a["market"])
        elif "BTC-" in a["market"]:
            BTCticker.append(a["market"])
        elif "USDT-" in a["market"]:
            USDTticker.append(a["market"])
    tickers = {"KRW": KRWticker,"BTC":BTCticker,"USD":USDTticker}
    return tickers[current]



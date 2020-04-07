import requests


def getTickersKraken(pair):
    krakenUrl = "https://api.kraken.com/0/public/Ticker"
    params = krakenUrl + "?pair=" + pair
    try:
        r = requests.get(params)
        ask_price = r.json()["result"][pair]["a"]
        bid_price = r.json()["result"][pair]["b"]
        # XXBTZEUR is BTCEUR, using ISO 4217 BTC is BTZ
        if pair == "XXBTZEUR" or pair == "XXBTZUSD":
            x = f'Ask price: {1} {pair[2:5]} = {round(float(ask_price[0]), 3)} {pair[5:8]}'
            y = f'Bid price: {1} {pair[2:5]} = {round(float(bid_price[0]), 3)} {pair[5:8]}'
            pairPrice = f'{x} \n{y}'
            print(pairPrice)
            return pairPrice
        else:
            x = f'Ask price: {1} {pair[1:4]} = {round(float(ask_price[0]), 3)} {pair[5:8]}'
            y = f'Bid price: {1} {pair[1:4]} = {round(float(bid_price[0]), 3)} {pair[5:8]}'
            pairPrice = f'{x} \n{y}'
            return pairPrice
    except ConnectionError:
        print(f"Connection problem: {ConnectionError}")


def getBinanceTicker(pair):
    binanceUrl = "https://api.binance.com/api/v3/ticker/bookTicker"
    params = binanceUrl + "?symbol=" + pair
    try:
        r = requests.get(params)
        askPrice = r.json()["askPrice"]
        bidPrice = r.json()["bidPrice"]
        #print(type(r.json()))
        x = f'Ask price: 1 {pair[0:3]} = {askPrice} {pair[3:6]}'
        y = f'Bid price: 1 {pair[0:3]} = {bidPrice} {pair[3:6]}'
        pairPrice = f'{x} \n{y}'
        return pairPrice
    except ConnectionError:
        print(f"Connection problem: {ConnectionError}")

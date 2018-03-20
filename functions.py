import json

import requests


def get_all_pumps():
    print "Downloading Data sets"
    data_set = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')
    data_set = json.loads(data_set.text)
    print "Analysing data sets "
    print "This routine will find Cryptos  with possibility of massive run-up/pump."
    for each_coin in data_set:
        if each_coin['24h_volume_usd'] and each_coin['market_cap_usd'] and each_coin['total_supply'] and float(
                each_coin['24h_volume_usd']) > float(each_coin['market_cap_usd']) and float(
                each_coin['total_supply']) > 800000000:
            print "Check out this coin : " + each_coin['name'] + "  " + each_coin['symbol']
            print "\t 24h Volume  "+each_coin['24h_volume_usd']
            print "\t Market Cap " + each_coin['market_cap_usd']
            print "\t Total supply " + each_coin['total_supply']




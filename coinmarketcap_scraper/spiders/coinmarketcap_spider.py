import json

from scrapy.spiders import Spider

from coinmarketcap_scraper.items import CoinItem


class CoinMarketCapSpider(Spider):
    name = 'coinmarketcap-spider'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    def parse(self, response, **kwargs):
        raw_coins = json.loads(response.css('#__NEXT_DATA__ ::text').get().encode('utf-8'))[
            'props']['initialState']['cryptocurrency']['listingLatest']['data']

        for raw_coin in raw_coins:
            coin = CoinItem()
            coin['name'] = raw_coin['name']
            coin['symbol'] = raw_coin['symbol']
            coin['price'] = raw_coin['quote']['USD']['price']
            coin['percentage_change_24h'] = raw_coin['quote']['USD']['percentChange24h']
            coin['percentage_change_7d'] = raw_coin['quote']['USD']['percentChange7d']
            coin['market_cap'] = raw_coin['quote']['USD']['marketCap']
            coin['volume'] = raw_coin['quote']['USD']['volume24h']
            coin['circulating_supply'] = raw_coin['circulatingSupply']
            coin['rank'] = raw_coin['cmcRank']
            coin['currency'] = raw_coin['quote']['USD']['name']

            yield coin

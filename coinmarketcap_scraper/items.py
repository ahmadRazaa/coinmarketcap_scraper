from scrapy.item import Item, Field


class CoinItem(Item):
    name = Field()
    symbol = Field()
    price = Field()
    percentage_change_24h = Field()
    percentage_change_7d = Field()
    market_cap = Field()
    volume = Field()
    circulating_supply = Field()
    rank = Field()
    currency = Field()

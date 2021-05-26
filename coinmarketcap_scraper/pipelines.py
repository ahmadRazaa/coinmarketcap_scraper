import sqlite3


class SQLitePipeline:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_spider(self, spider):
        self.create_connection()
        self.create_tables()

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def create_connection(self):
        self.connection = sqlite3.connect('coinmarketcap.db')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS coins (
            id integer PRIMARY KEY,
            coin_name VARCHAR(80) NOT NULL UNIQUE, 
            coin_symbol VARCHAR(3) NOT NULL UNIQUE);"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS market_data (
            id integer PRIMARY KEY,
            coin_id INTEGER references coins(id), 
            price DECIMAL(18, 2),
            percentage_change_24h DECIMAL(18, 2),
            percentage_change_7d DECIMAL(18, 2),
            market_cap DECIMAL(18, 2),
            volume DECIMAL(18, 2),
            circulating_supply DECIMAL(18, 2),
            rank INTEGER ,
            currency VARCHAR(10),
            crawled_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );"""
        )

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (item['name'], item['symbol'])
        sql = 'INSERT OR IGNORE INTO coins(coin_name, coin_symbol) VALUES(?,?) '
        self.cursor.execute(sql, values)

        self.cursor.execute(f'SELECT id FROM coins WHERE coins.coin_name = \"{item["name"]}\"')
        coin_id = self.cursor.fetchall()[0][0]

        values = (
            coin_id, item['price'], item['percentage_change_24h'],
            item['percentage_change_7d'], item['market_cap'], item['volume'],
            item['circulating_supply'], item['rank'], item['currency']
        )
        sql = 'INSERT INTO market_data(coin_id, price, percentage_change_24h,' \
              ' percentage_change_7d, market_cap, volume, circulating_supply, rank, currency) VALUES(?,?,?,?,?,?,?,?,?)'
        self.cursor.execute(sql, values)

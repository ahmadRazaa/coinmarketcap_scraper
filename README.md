# CoinMarketCap.com Scraper 

## Installation

tested with Python 3.7.3+
- create a virtual environment
- clone repo `git clone https://github.com/ahmadRazaa/coinmarketcap_scraper.git`
- move to project directory `cd coinmarketcap_scraper`
- install dependencies by `pip install -r requirements.txt`


## Running Spider

run spider by `scrapy crawl coinmarketcap-spider`

to save data in JSON file `scrapy crawl coinmarketcap-spider -o coins.json`

to save data in CSV file `scrapy crawl coinmarketcap-spider -o coins.csv`

NOTE: each time spider is executed, new data is inserted into the SQLite DB
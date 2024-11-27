coins = [
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "fraud": False,
        "test": False,
        "max_market_cap_e9": 1_800.0,
        "start_date": "2014-11-01",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "Bitcoin",
            "wallstreetbets",
            "Superstonk",
        ],
    },
    {
        "name": "Ethereum",
        "symbol": "ETH",
        "fraud": False,
        "test": True,
        "max_market_cap_e9": 550.0,
        "start_date": "2016-02-18",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "ethereum",
            "ethtrader",
            "Superstonk",
        ],
    },
    {
        "name": "Terra Luna",
        "symbol": "LUNC",
        "fraud": True,
        "test": False,
        "max_market_cap_e9": 41.0,
        "start_date": "2019-07-07",
        "end_date": "2022-05-08",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "terraluna",
            "CryptoCurrencyClassic",
            "Crypto_General",
            "LunaClassic",
            "Gemini",
        ],
    },
    {
        "name": "Avalanche",
        "symbol": "AVAX",
        "fraud": False,
        "test": False,
        "max_market_cap_e9": 30.0,
        "start_date": "2020-09-23",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "Avax",
            "CryptoBreakingDotCom",
            "Thecoinrise",
            "Crypto_General",
            "CryptoCurrencyClassic",
            "cryptonewsland",
        ],
    },
    {
        "name": "Cosmos",
        "symbol": "ATOM",
        "fraud": False,
        "test": True,
        "max_market_cap_e9": 11.0,
        "start_date": "2019-03-15",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "cosmosnetwork",
            "CoinBase",
            "CryptoBreakingDotCom",
            "CryptoEducationHub",
            "Blofin",
            "ledgerwallet",
            "kryptomaniak",
        ],
    },
    {
        "name": "Chainlink",
        "symbol": "LINK",
        "fraud": False,
        "test": False,
        "max_market_cap_e9": 9.9,
        "start_date": "2017-10-01",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "ethtrader",
            "Chainlink",
            "ethereum",
            "LINKTrader",
        ],
    },
    {
        "name": "FTX Token",
        "symbol": "FTT",
        "fraud": True,
        "test": True,
        "max_market_cap_e9": 9.5,
        "start_date": "2019-08-01",
        "end_date": "2022-11-07",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "Superstonk",
            "Nexo",
            "SafeMoon",
            "ftx"
        ],
    },
    
    {
        "name": "THORChain",
        "symbol": "RUNE",
        "fraud": False,
        "test": False,
        "max_market_cap_e9": 1.8,
        "start_date": "2019-07-24",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "getagraph",
            "THORChain",
            "Monero",
            "cosmosnetwork",
            "cryptoloversclub",
            "lolacoin",
            "CryptoBreakingDotCom",
            "Crypto_General",
        ],
    },
    {
        "name": "BeerCoin",
        "symbol": "BEER",
        "fraud": True,
        "test": False,
        "max_market_cap_e9": 0.31,
        "start_date": "2024-05-27",
        "end_date": "2024-06-24",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "wallstreetbetsGER",
            "memecoins",
            "Kryptostrassenwetten",
            "SolCoins",
            "bitpanda",
            "Memecoinhub",
        ],
    },
    {
        "name": "BitForex",
        "symbol": "BF",
        "fraud": True,
        "test": False,
        "max_market_cap_e9": 0.057,
        "start_date": "2019-08-31",
        "end_date": "2024-03-05",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "ecomi",
            "CryptoExchange",
            "SafeMoon",
            "BitForex",
            "Superstonk",
            "CryptoCurrencyClassic",
        ],
    },
    {
        "name": "Safe Moon",
        "symbol": "SAFEMOON",
        "fraud": True,
        "test": True,
        "max_market_cap_e9": 0.0,
        "start_date": "2022-01-17",
        "end_date": "2023-10-31",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "SafeMoon",
        ],
    },
    {
        "name": "Teddy Doge",
        "symbol": "TEDDY V2",
        "fraud": True,
        "test": False,
        "max_market_cap_e9": 0.0,
        "start_date": "2022-06-28",
        "end_date": "2022-07-21",
        "subreddits": [
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
            "coinmarketbag",
            "cryptopricesalerts",
            "CoinMarketDo",
            "dogecoin",
            "kryptocal",
        ],
    },
    {
        "name": "STOA Network",
        "symbol": "STA",
        "fraud": True,
        "test": False,
        "max_market_cap_e9": 0.0,
        "start_date": "2021-12-28",
        "end_date": "2022-07-17",
        "subreddits": [
            "BitMartExchange",
            "CryptoCurrency",
            "CryptoMoonShots",
            "CryptoMarkets",
            "Crypto",
        ],
    },
]

import pandas as pd

df = pd.DataFrame(coins)
df.to_json("data/raw/coins.json", orient="records")

\# Trading Bot — Binance Futures Testnet



Setup

1\. Install: pip install -r requirements.txt

2\. Create .env file with API\_KEY and API\_SECRET

3\. Register at https://testnet.binancefuture.com





Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01



Limit Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 50000



Assumption : : 

\- Uses Binance USDT-M Futures Testnet only

\- Minimum quantity for BTCUSDT is 0.001

\- Uses System Generated HMAC API keys


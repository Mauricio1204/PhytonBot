import yfinance as yf

def yahoo_backtest():
    try:
        data = yf.download('BTC-USD', period='1mo', auto_adjust=False)
        print(data)
    except Exception as e:
        print("Error al obtener datos de BTC-USD:", e)

import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

def run_backtest(csv_path='data/BTCUSDT_4h_data.csv', cash=100000, commission=0.002):
    # Cargar datos usando la columna 'Open time' como fecha
    df = pd.read_csv(csv_path)
    df['Open time'] = pd.to_datetime(df['Open time'])
    df.rename(columns={
        'Open time': 'Date',
        'Open': 'Open',
        'High': 'High',
        'Low': 'Low',
        'Close': 'Close',
        'Volume': 'Volume'
    }, inplace=True)

    # Filtrar solo las columnas necesarias para el backtest
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df.set_index('Date', inplace=True)

    # Definir estrategia
    class SmaCross(Strategy):
        n1 = 10
        n2 = 30

        def init(self):
            self.sma1 = self.I(SMA, self.data.Close, self.n1)
            self.sma2 = self.I(SMA, self.data.Close, self.n2)

        def next(self):
            if crossover(self.sma1, self.sma2):
                self.buy(size=1)
            elif crossover(self.sma2, self.sma1):
                self.sell(size=1)

    # Ejecutar backtest
    bt = Backtest(df, SmaCross, cash=cash, commission=commission)
    stats = bt.run()
    print(stats)
    bt.plot()

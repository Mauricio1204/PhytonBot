import yfinance as yf
import ta.trend
import pandas as pd
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting import Backtest

class SMAcross(Strategy):
    # Señal de compra cuando SMA rapida n1 cruza por encima de SMA lenta n2, caso contrario para entradas en corto
    # Variables a testear  
    n1 = 100 
    n2 = 50
    risk_per_trade = 0.05
    stop_loss_pct = 0.05
    take_profit_pct = 0.10

    def init(self):
        if self.n1 <= self.n2:
            raise ValueError("n1 (SMA rápida) debe ser menor que n2 (SMA lenta)")
        
        # Indicadores de medias móviles
        close = self.data.Close
        self.sma1 = self.I(ta.trend.sma_indicator, close, self.n1)
        self.sma2 = self.I(ta.trend.sma_indicator, close, self.n2)

        self.current_sl = None
        self.current_tp = None

    def next(self):

        price = self.data.Close[-1] #precio de cierre actual

        if not self.position:
            #Cruce alcista
            if crossover(self.sma1, self.sma2):
                self.current_sl = price * (1 - self.stop_loss_pct)
                self.current_tp = price * (1 + self.take_profit_pct)
                self.buy(sl=self.current_sl, tp=self.current_tp)
                self.set_log(f"Comprando a {price:.2f}, SL: {self.current_sl:.2f}, TP: {self.current_tp:.2f}")

            elif crossover(self.sma2, self.sma1):
            #Cruce bajista
                self.current_sl = price * (1 + self.stop_loss_pct) 
                self.current_tp = price * (1 - self.take_profit_pct) 
                self.sell(sl=self.current_sl, tp=self.current_tp)
                self.set_log(f"Vendiendo en corto a {price:.2f}, SL: {self.current_sl:.2f}, TP: {self.current_tp:.2f}")
        
        # Logica de cierre de posiciones existentes por cruce inverso
        else:
            if self.position.is_long:
                if crossover(self.sma2, self.sma1):
                    self.position.close()
                    self.set_log(f"Cerrando posicion larga a {price:.2f} por cruce bajista")

            elif self.position.is_short:
                if crossover(self.sma1, self.sma2):
                    self.position.close()
                    self.set_log(f"Cerrando posicion corta a {price:0.2f} por cruce alcista")

if __name__ == '__main__':
    symbol = "BTC-USD"
    period = "1mo"
    auto_adjust = False
    data = yf.download(symbol, period=period, auto_adjust=auto_adjust)
    
    data.columns = [col[1][0] if isinstance(col, tuple) else col for col in data.columns]

    print( data.columns )
    
    # Solo deja las columnas necesarias
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    missing = [col for col in required_cols if col not in data.columns]
    if missing:
        raise ValueError(f"Faltan columnas necesarias: {missing}")
    
    data = data[required_cols]

    bt = Backtest(data, SMAcross,
                  cash=10000,        
                  commission=0.002,    
                  exclusive_orders=True) # Solo una orden por barra

    stats = bt.run()
    print("\n--- Resultados del Backtest ---")
    print(stats)

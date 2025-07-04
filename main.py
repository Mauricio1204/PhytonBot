from account.saldo import mostrar_balance_futuros_usdt
from account.saldo_spot import mostrar_balance_spot_usdt
from estrategias.crossover import run_backtest
from pruebas.yahoo import yahoo_backtest

if __name__ == '__main__':
    yahoo_backtest()
    #run_backtest()
    #mostrar_balance_futuros_usdt()
    #mostrar_balance_spot_usdt()
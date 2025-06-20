import os
from dotenv import load_dotenv
from binance.client import Client
from rich.console import Console

# Cargar consola
console = Console()

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
client = Client(api_key, api_secret)

def mostrar_balance_futuros_usdt():
    try:
        balance_futuros = client.futures_account_balance()
        for asset in balance_futuros:
            if asset['asset'] == 'USDT':
                console.print(f"USDT Futuros disponible: {asset['availableBalance']} USD", style="bold green")
                if float(asset['availableBalance']) >= 10:
                    console.print("Tienes USDT disponibles para operar en Futuros.", style="bold white")
                else:
                    console.print("No tienes USDT suficientes para operar en Futuros.", style="bold red")
                break
        else:
            print("No se encontró USDT en tu cuenta de Futuros.")
    except Exception as e:
        print("Error al obtener el balance de Futuros:", e)

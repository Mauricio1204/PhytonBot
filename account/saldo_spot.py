import os
from dotenv import load_dotenv
from binance.client import Client
from rich.console import Console

#Cargar console.
console = Console()

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
client = Client(api_key, api_secret)

def mostrar_balance_spot_usdt():
    try:
        usdt_balance = client.get_asset_balance(asset='USDT')
        if usdt_balance:
            console.print(f"USDT Spot disponible: {usdt_balance['free']} USD", style="bold green")
            if float(usdt_balance['free']) >= 10:
                console.print("Tienes USDT disponibles.", style="bold white")
            else:
                console.print("No tienes USDT disponible para operar.", style="bold red")
        else:
            print("No se encontró USDT en tu cuenta Spot.")
    except Exception as e:
        print("Error al obtener el balance Spot:", e)
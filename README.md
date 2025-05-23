# PhytonBot
Criptomonedas 
bitcoin-futures-bot/
│
├── data/                       # Almacena datos crudos e intermedios
│   ├── historical/             # Datos históricos de precios
│   ├── news/                   # Noticias procesadas
│   └── processed/              # Datos preprocesados para entrenamiento
│
├── notebooks/                 # Notebooks Jupyter para análisis exploratorio
│
├── models/                    # Modelos de IA entrenados y scripts de entrenamiento
│   ├── training/              # Scripts para entrenamiento de modelos
│   ├── inference/             # Scripts para hacer predicciones
│   └── saved/                 # Modelos entrenados guardados
│
├── bot/                       # Lógica del bot de trading
│   ├── strategy/              # Estrategias de trading (basadas en IA o reglas)
│   ├── broker_api/            # Conexión a exchanges (ej. Binance, Bybit)
│   └── execution/             # Módulos de ejecución de órdenes y control de riesgo
│
├── news_scraper/              # Código para recopilar y analizar noticias
│   ├── sources/               # Scrapers por fuente (ej. Twitter, CoinDesk)
│   └── sentiment_analysis/    # Análisis de sentimiento con NLP
│
├── utils/                     # Funciones generales (log, manejo de fechas, etc.)
│
├── config/                    # Configuraciones por entorno (API keys, parámetros)
│
├── tests/                     # Pruebas unitarias y de integración
│
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Variables de entorno (API keys, etc.)
├── README.md                  # Explicación del proyecto
└── main.py                    # Script principal que corre el bot

import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

transport = json.load(open('./data.json'))['transport']

app = FastAPI()

origins = ["http://localhost:8080", "127.0.0.1:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_transport():
    # Get all cities from data.json and uses
    # set() to erase duplicates.
    cities = set([item['city'] for item in transport])
    return cities


@app.get("/city/{city}")
def get_prices(city: str):
    # Get all options of transport for the chosen city.
    options = [item for item in transport if item['city'] == city]

    # Get all durations and prices, turning them to integer
    # and float respectively.
    durations = [int(item['duration'].replace('h', '')) for item in options]
    prices = [float(item['price_econ'].split('R$ ')[1].replace(',', '.'))
              for item in options]

    # Uses min() to find the fastest and cheapest options,
    # and then uses its indexes to find the original objects.
    fastest = options[durations.index(min(durations))]
    cheapest = options[prices.index(min(prices))]

    return [{
            'name': fastest['name'],
            'type': 'confort',
            'description': 'Leito: ' + fastest['bed'],
            'duration': fastest['duration'],
            'price': fastest['price_confort']
            },
            {
            'name': cheapest['name'],
            'type': 'economic',
            'description': 'Poltrona: ' + cheapest['seat'],
            'duration': cheapest['duration'],
            'price': cheapest['price_econ']
            }]

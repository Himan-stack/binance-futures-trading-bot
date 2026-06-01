# Binance Futures Testnet Trading Bot

A simple Python CLI-based trading bot for Binance Futures Testnet using direct REST API integration.

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* Input validation using argparse
* Logging of API requests and responses
* Exception handling for invalid inputs and API failures
* Structured project architecture

---

## Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── cli.py
│   └── __init__.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.\venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

## Run Examples

### MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Logging

Logs are stored inside:

```bash
logs/trading_bot.log
```

---

## Assumptions

* Binance Futures Testnet account is configured
* API keys are valid
* Internet connection is available
* Testnet balance is available

---

## Technologies Used

* Python 3
* Requests
* argparse
* dotenv
* Binance Futures Testnet REST API

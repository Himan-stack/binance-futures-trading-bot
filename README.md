# Binance Futures Trading Bot 📈

**REST API-driven trading bot with production-grade authentication & modular architecture**

A lightweight Python CLI tool for Binance Futures Testnet that demonstrates **real API integration, HMAC-SHA256 authentication, and backend best practices**. This isn't a get-rich-quick trading strategy—it's a learning project focused on API fundamentals and clean code.

---

## 🎯 Why I Built This

**Motivation:** Deep understanding of:
- REST API design and authentication (HMAC-SHA256)
- Production-grade backend development
- Secure credential handling (environment variables)
- Modular, testable Python architecture
- Real financial data handling

**Result:** Successfully executed MARKET and LIMIT orders on Binance Futures Testnet. Learned what it takes to build reliable backend systems.

---

## ✅ Live Test Results

| Test Case | Status | Details |
|-----------|--------|---------|
| MARKET BUY (BTCUSDT) | ✅ Success | Executed 0.001 BTC |
| LIMIT SELL (BTCUSDT) | ✅ Success | Set limit at $120k, validated |
| API Authentication | ✅ Success | HMAC-SHA256 signatures validated |
| Order Validation | ✅ Success | 5+ edge cases handled |
| Error Recovery | ✅ Success | Graceful handling of invalid keys, bad endpoints |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              CLI Interface (argparse)               │
│  --symbol BTCUSDT --side BUY --quantity 0.001       │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│            Input Validators (validators.py)         │
│  - Symbol format (XXUSDT)                           │
│  - Quantity precision (min/max)                     │
│  - Price levels (for LIMIT orders)                  │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│         Binance API Client (client.py)              │
│  - HMAC-SHA256 signature generation                 │
│  - Request/response handling                        │
│  - Error classification (auth vs API vs network)    │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│         Order Management (orders.py)                │
│  - MARKET order creation                            │
│  - LIMIT order creation with validation             │
│  - Response parsing & logging                       │
└──────────────────┬──────────────────────────────────┘
                   │
           Binance Futures API
        https://testnet.binancefuture.com
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Binance Futures Testnet account (free)
- API key + Secret key from Binance

### Setup

```bash
# Clone
git clone https://github.com/Himan-stack/binance-futures-trading-bot.git
cd binance-futures-trading-bot

# Virtual environment
python -m venv venv

# Activate
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install
pip install -r requirements.txt

# Configure .env file
echo "BINANCE_API_KEY=your_key" > .env
echo "BINANCE_SECRET_KEY=your_secret" >> .env
echo "BASE_URL=https://testnet.binancefuture.com" >> .env
```

### Execute Orders

**MARKET Order:**
```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

**LIMIT Order:**
```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

**Output:**
```
[INFO] Connecting to Binance Futures Testnet...
[INFO] Validating order parameters...
[INFO] Generating HMAC-SHA256 signature...
[SUCCESS] Order executed: Order ID 12345
[LOG] Saved to logs/trading_bot.log
```

---

## 📁 Project Structure

```
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py              # API client (authentication, requests)
│   ├── orders.py              # Order creation logic
│   ├── validators.py          # Input validation
│   ├── logging_config.py      # Structured logging setup
│   └── cli.py                 # CLI argument parsing
│
├── logs/
│   └── trading_bot.log        # All API calls & responses logged
│
├── main.py                    # Entry point
├── requirements.txt
├── .env                       # (Create this with your credentials)
└── README.md
```

---

## 🔐 Security & Authentication

### HMAC-SHA256 Signature Generation

```python
# How it works:
timestamp = current_time_ms
query_string = f"symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.001&timestamp={timestamp}"
signature = hmac.new(
    SECRET_KEY.encode(),
    query_string.encode(),
    hashlib.sha256
).hexdigest()

# Add to header: X-MBX-APIKEY: {API_KEY}
# Add to request: &signature={signature}
```

**Security Notes:**
- ✅ Never hardcode credentials (uses `.env`)
- ✅ Signature changes per request (timestamp prevents replay attacks)
- ✅ API key stored server-side, not in code
- ✅ All requests logged (for audit trails)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **API Integration** | `requests` library |
| **Authentication** | HMAC-SHA256 (hashlib) |
| **CLI** | argparse |
| **Credentials** | python-dotenv |
| **Logging** | structured logging (JSON format) |
| **Testing** | pytest (basic validation) |

---

## 🐛 Bugs Fixed During Development

| Issue | Root Cause | Solution |
|-------|-----------|----------|
| Invalid signature | Incorrect timestamp format | Used milliseconds, not seconds |
| 401 Unauthorized | Wrong API key source | Validated `.env` file existence |
| Testnet vs Live endpoint | Hardcoded production URL | Made BASE_URL configurable |
| LIMIT order rejected | Missing `timeInForce` parameter | Added `GTC` (Good Till Cancelled) |
| Module not found | Incorrect import paths | Fixed relative imports with `__init__.py` |
| GitHub conflicts | Merge conflicts on main | Learned: always branch before changes |

**Lesson:** Every bug fixed taught me something about production systems—error handling, logging, and deployment concerns matter as much as the core logic.

---

## 📚 Learnings & Insights

### API Design
- ✅ RESTful principles (HTTP verbs, status codes, error responses)
- ✅ Authentication (API keys, HMAC signatures, bearer tokens)
- ✅ Rate limiting & exponential backoff
- ✅ Idempotency for financial transactions

### Backend Development
- ✅ Modular architecture (separation of concerns)
- ✅ Configuration management (environment variables)
- ✅ Logging & observability (what happened and why)
- ✅ Error handling (validation → execution → recovery)

### Financial Systems
- ✅ Order types (MARKET, LIMIT, STOP)
- ✅ Position management (margin, leverage)
- ✅ Risk controls (position sizing, stop-loss)
- ✅ Testnet vs production (dry-run before real money)

---

## 🚨 Important Notes

- **Testnet only:** This uses Binance Futures Testnet (fake money). Real money trading requires additional risk controls.
- **Educational tool:** Not designed for live trading strategies. Use for learning API integration and backend development.
- **Rate limits:** Binance has rate limits. Respect them.
- **No financial advice:** I don't provide trading strategies or market predictions.

---

## 🔧 Advanced: Custom Strategies

Want to build a real trading strategy? Here's the pattern:

```python
# 1. Fetch market data
ohlcv = client.fetch_ohlcv('BTCUSDT', timeframe='1h', limit=100)

# 2. Generate signals (your logic here)
signal = your_strategy_function(ohlcv)

# 3. Execute order
if signal == 'BUY':
    orders.place_market_order('BTCUSDT', 'BUY', quantity)
elif signal == 'SELL':
    orders.place_market_order('BTCUSDT', 'SELL', quantity)

# 4. Logging & monitoring
log_trade(order_id, timestamp, price, quantity)
```

---

## 📞 Contact

**Email:** himanshubg70@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/himanshu-kumar-076a13321/  
**GitHub:** https://github.com/Himan-stack

---

**Built to learn REST APIs, authentication, and backend development.**  
*Not a trading algorithm. Just clean code and real API integration.*

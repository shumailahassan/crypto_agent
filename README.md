# 💰 Crypto Price Agent (Chainlit)

This is a simple cryptocurrency price agent built using **Chainlit** and **Coingecko API**. The agent allows users to check real-time prices of **Bitcoin (BTC)** and **Ethereum (ETH)** through a conversational interface.

---

## 🚀 Features

- ✅ Real-time price data using Coingecko API
- ✅ Simple user interface via Chainlit
- ✅ Supports basic queries like:
  - "What is the price of Bitcoin?"
  - "BTC ka rate kya hai?"
  - "Tell me Ethereum price"

---

## 🛠️ Tech Stack

- [Chainlit](https://www.chainlit.io/) - Chat UI framework
- [Python](https://www.python.org/)
- [Coingecko API](https://www.coingecko.com/en/api/documentation) - Public crypto data

---

## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/crypto_agent.git
cd crypto_agent

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Chainlit app
chainlit run main.py

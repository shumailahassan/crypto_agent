import chainlit as cl
import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.lower()

    if "price" in user_input:
        if "bitcoin" in user_input or "btc" in user_input:
            coin = "bitcoin"
        elif "ethereum" in user_input or "eth" in user_input:
            coin = "ethereum"
        else:
            await cl.Message(content="Please mention 'bitcoin' or 'ethereum'.").send()
            return

        params = {
            "ids": coin,
            "vs_currencies": "usd"
        }

        response = requests.get(API_URL, params=params)
        data = response.json()

        if coin in data:
            price = data[coin]['usd']
            await cl.Message(content=f"💰 Current price of **{coin.capitalize()}** is **${price}**").send()
        else:
            await cl.Message(content="Failed to fetch price. Try again later.").send()
    else:
        await cl.Message(content="❓ You can ask me: 'What is the price of Bitcoin?'").send()

import yfinance as yf
import pandas as pd

# Fetch data (Nasdaq futures proxy)
symbol = "NQ=F"

# Get recent 5-minute data
df = yf.download(symbol, interval="5m", period="5d")

# Keep only last 200 rows
df = df.tail(200)

# Save to CSV
filename = "nq_data.csv"
df.to_csv(filename)

print(f"Saved to {filename}")
print(df.tail())

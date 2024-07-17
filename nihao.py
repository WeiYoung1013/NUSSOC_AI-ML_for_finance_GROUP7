import yfinance as yf
import pandas as pd
from datetime import datetime

# 标准普尔500指数成分股代码列表
sp500_symbols = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'BRK-A', 'BRK-B', 'JNJ', 'TSLA',
    'V', 'WMT', 'JPM', 'MA', 'PG', 'NVDA', 'HD', 'DIS', 'UNH', 'PYPL', 'BAC', 'INTC',
    'CMCSA', 'VZ', 'NFLX', 'PFE', 'ADBE', 'T', 'PEP', 'CRM', 'ABT', 'CSCO', 'ABBV',
    'XOM', 'AVGO', 'KO', 'CMG', 'AMD', 'DUK', 'QCOM', 'TMO', 'COST', 'LLY', 'NEE',
    'MRK', 'MDT', 'TMUS', 'ORCL', 'ACN', 'NKE', 'CL'
]

class StockAnalyzer:
    def __init__(self):
        self.top_50_stocks = self.get_top_50_stocks()
        self.stock_data = self.get_stock_data(self.top_50_stocks)

    def get_top_50_stocks(self):
        market_caps = {}
        for symbol in sp500_symbols:
            stock = yf.Ticker(symbol)
            info = stock.info
            if 'marketCap' in info and info['marketCap'] is not None:
                market_cap = info['marketCap']
                # 修正 AVGO 市值问题
                if symbol == 'AVGO':
                    market_cap /= 10
                market_caps[symbol] = market_cap

        sorted_market_caps = {k: v for k, v in sorted(market_caps.items(), key=lambda item: item[1], reverse=True)}
        top_50_stocks = list(sorted_market_caps.keys())[:50]
        return top_50_stocks

    def get_stock_data(self, tickers):
        stock_data = []
        for ticker in tickers:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="5d")  # 获取最近2天的数据
            if len(hist) >= 2:
                prev_data = hist.iloc[-2]
                latest_data = hist.iloc[-1]
                growth_amount = float(latest_data['Close'] - prev_data['Close'])
                growth_rate = float(growth_amount / prev_data['Close'])
                market_cap = stock.info.get('marketCap', 0)
                # 修正 AVGO 市值问题
                if ticker == 'AVGO':
                    market_cap /= 10
                date_str = latest_data.name.strftime('%Y/%m/%d')
                stock_data.append([
                    date_str,
                    ticker,
                    float(latest_data['Open']),
                    float(latest_data['Close']),
                    float(latest_data['High']),
                    float(latest_data['Low']),
                    growth_amount,
                    growth_rate,
                    market_cap
                ])
        return stock_data

    def get_top_10_by_growth_amount(self):
        sorted_data = sorted(self.stock_data, key=lambda x: x[6], reverse=True)  # 根据增长量排序
        return sorted_data[:10]

    def get_top_10_by_growth_rate(self):
        sorted_data = sorted(self.stock_data, key=lambda x: x[7], reverse=True)  # 根据增长率排序
        return sorted_data[:10]

    def get_top_10_by_market_cap(self):
        sorted_data = sorted(self.stock_data, key=lambda x: x[8], reverse=True)  # 根据市值排序
        return sorted_data[:10]

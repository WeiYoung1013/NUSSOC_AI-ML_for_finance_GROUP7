import yfinance as yf
import pandas as pd

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
            hist = stock.history(period="5d")  # 获取最近5天的数据，确保有足够的历史数据
            if len(hist) >= 2:
                prev_close = hist['Close'].iloc[-2]
                latest_close = hist['Close'].iloc[-1]
                growth_amount = latest_close - prev_close
                growth_rate = growth_amount / prev_close
                market_cap = stock.info['marketCap']
                # 修正 AVGO 市值问题
                if ticker == 'AVGO':
                    market_cap /= 10
                stock_data.append({
                    'ticker': ticker,
                    'prev_close': prev_close,
                    'latest_close': latest_close,
                    'growth_amount': growth_amount,
                    'growth_rate': growth_rate,
                    'market_cap': market_cap
                })
        df = pd.DataFrame(stock_data)
        return df

    def get_top_10_by_growth_amount(self):
        top_10_growth_amount = self.stock_data.nlargest(10, 'growth_amount')
        return top_10_growth_amount

    def get_top_10_by_growth_rate(self):
        top_10_growth_rate = self.stock_data.nlargest(10, 'growth_rate')
        return top_10_growth_rate

    def get_top_10_by_market_cap(self):
        top_10_market_cap = self.stock_data.nlargest(10, 'market_cap')
        return top_10_market_cap

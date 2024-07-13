import os
import yfinance as yf
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def xgboost_trading_strategy(tickers, initial_cash=10000, investment_percentage=0.15, window_size=5):
    # 设置日期
    start_train = '2019-01-01'
    end_train = '2023-12-31'
    start_test = '2024-01-01'
    end_test = '2024-12-31'
    
    # 获取数据
    def download_data(ticker, start, end):
        df = yf.download(ticker, start=start, end=end)
        df['Change'] = df['Close'].pct_change()
        df = df.dropna()
        return df

    # 数据预处理和特征构造
    def create_dataset(df, window_size=5):
        data = df['Change'].values
        X, y = [], []
        for i in range(len(data) - window_size):
            X.append(data[i:i + window_size])
            y.append(data[i + window_size])
        return np.array(X), np.array(y)

    cash = initial_cash
    positions = {ticker: 0 for ticker in tickers}
    cash_history = []

    # 获取并处理数据
    train_data = {}
    test_data = {}
    for ticker in tickers:
        try:
            train_data[ticker] = download_data(ticker, start_train, end_train)
            test_data[ticker] = download_data(ticker, start_test, end_test)
        except Exception as e:
            print(f"Failed to download {ticker}: {e}")
            tickers.remove(ticker)

    # 获取基准数据（例如S&P 500）
    benchmark = yf.download('^GSPC', start=start_test, end=end_test)
    benchmark['Return'] = benchmark['Close'].pct_change().dropna()

    # 训练和预测
    predictions_dict = {}
    for ticker in tickers:
        df_train = train_data[ticker]
        df_test = test_data[ticker]

        X_train, y_train = create_dataset(df_train, window_size)
        X_test, y_test = create_dataset(df_test, window_size)

        # XGBoost requires 2D input
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1]))
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1]))

        model = xgb.XGBRegressor(objective='reg:squarederror')
        model.fit(X_train, y_train)

        predictions = model.predict(X_test).flatten()
        df_test = df_test.iloc[window_size:]
        df_test['Predicted_Change'] = predictions
        predictions_dict[ticker] = df_test

    # 创建测试日期范围
    test_dates = predictions_dict[tickers[0]].index

    # 回测策略
    daily_returns = []
    for date in test_dates:
        day_cash = cash
        for ticker in tickers:
            if date in predictions_dict[ticker].index:
                df_test = predictions_dict[ticker]
                if df_test.loc[date, 'Predicted_Change'] > 0:
                    if positions[ticker] == 0:
                        investment = cash * investment_percentage
                    else:
                        investment = positions[ticker] * df_test.loc[date, 'Close'] * investment_percentage

                    if cash >= investment:
                        cash -= investment
                        positions[ticker] += investment / df_test.loc[date, 'Close']

                elif df_test.loc[date, 'Predicted_Change'] < 0 and positions[ticker] > 0:
                    investment = positions[ticker] * df_test.loc[date, 'Close'] * investment_percentage
                    cash += investment
                    positions[ticker] -= investment / df_test.loc[date, 'Close']

        portfolio_value = cash + sum([positions[t] * predictions_dict[t].loc[date, 'Close'] for t in tickers])
        daily_returns.append((portfolio_value - initial_cash) / initial_cash)
        cash_history.append(portfolio_value)

    # 确保cash_history和日期范围长度一致
    dates = test_dates[:len(cash_history)]

    # 计算策略收益率
    strategy_returns = np.diff(cash_history) / cash_history[:-1]

    # 绘制现金历史曲线并保存图片
    plt.figure(figsize=(12, 6))
    plt.plot(dates, cash_history, label='Portfolio Value')
    plt.title('Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    image_path = 'images/portfolio_value_xgboost.png'
    plt.savefig(os.path.join('static', image_path))
    plt.close()

    # 计算Sharpe Ratio
    risk_free_rate = 0.01
    excess_returns = strategy_returns - risk_free_rate / 252
    sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)

    # 计算Alpha和Beta
    benchmark_returns = benchmark['Return'][benchmark.index.isin(dates)]
    benchmark_returns = benchmark_returns.iloc[:len(strategy_returns)]  # 确保长度一致
    beta, alpha = np.polyfit(benchmark_returns, strategy_returns, 1)
    alpha = alpha * 252  # 年化Alpha

    # 计算最终收益
    final_cash = cash_history[-1]
    return_rate = (final_cash - initial_cash) / initial_cash * 100

    return return_rate, sharpe_ratio, alpha, beta, image_path



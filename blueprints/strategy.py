from flask import Blueprint, jsonify, request, session
from extends import db
from models import UserModel, UserStockSelection
from LSTMforStocks import lstm_trading_strategy
from lightGBMforStocks import lightgbm_trading_strategy
from XGBoostforStocks import xgboost_trading_strategy

st = Blueprint('st', __name__, url_prefix="/strategy")

@st.route('', methods=['POST'])
def strategy():
    stocks = [
        'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'BRK-A', 'BRK-B', 'JNJ', 'TSLA',
        'V', 'WMT', 'JPM', 'MA', 'PG', 'NVDA', 'HD', 'DIS', 'UNH', 'PYPL', 'BAC', 'INTC',
        'CMCSA', 'VZ', 'NFLX', 'PFE', 'ADBE', 'T', 'PEP', 'CRM', 'ABT', 'CSCO', 'ABBV',
        'XOM', 'AVGO', 'KO', 'CMG', 'AMD', 'DUK', 'QCOM', 'TMO', 'COST', 'LLY', 'NEE',
        'MRK', 'MDT', 'TMUS', 'ORCL', 'ACN', 'NKE', 'CL'
    ]

    data = request.json
    selected_stocks = data.get('stocks')
    backtest_start_date = data.get('backtest_start_date')
    backtest_end_date = data.get('backtest_end_date')
    if len(selected_stocks) > 5:
        return jsonify({"error": "You can select up to 5 stocks only."}), 400

    # 处理用户选择的股票逻辑
    selected_stocks_str = ','.join(selected_stocks)
    user_name = session.get('user_name')
    if not user_name:
        return jsonify({"error": "User not logged in."}), 401

    selection = UserStockSelection(user_name=user_name, stock_symbol=selected_stocks_str)
    db.session.add(selection)
    db.session.commit()
    if not selected_stocks:
        return jsonify({"error": "No stocks selected."}), 400

    # 调用策略分析函数
    lstm_return_rate, lstm_sharpe_ratio, lstm_alpha, lstm_beta, lstm_image_path = lstm_trading_strategy(tickers=selected_stocks, start_test=backtest_start_date, end_test=backtest_end_date)
    lightgbm_return_rate, lightgbm_sharpe_ratio, lightgbm_alpha, lightgbm_beta, lightgbm_image_path = lightgbm_trading_strategy(tickers=selected_stocks, start_test=backtest_start_date, end_test=backtest_end_date)
    xgboost_return_rate, xgboost_sharpe_ratio, xgboost_alpha, xgboost_beta, xgboost_image_path = xgboost_trading_strategy(tickers=selected_stocks, start_test=backtest_start_date, end_test=backtest_end_date)
    
    results = {
        "LSTM": {
            "return_rate": lstm_return_rate,
            "sharpe_ratio": lstm_sharpe_ratio,
            "alpha": lstm_alpha,
            "beta": lstm_beta,
            "image_path": lstm_image_path
        },
        "lightGBM": {
            "return_rate": lightgbm_return_rate,
            "sharpe_ratio": lightgbm_sharpe_ratio,
            "alpha": lightgbm_alpha,
            "beta": lightgbm_beta,
            "image_path": lightgbm_image_path
        },
        "XGBoost": {
            "return_rate": xgboost_return_rate,
            "sharpe_ratio": xgboost_sharpe_ratio,
            "alpha": xgboost_alpha,
            "beta": xgboost_beta,
            "image_path": xgboost_image_path
        }
    }
    
    best_model = max(results, key=lambda x: results[x]['return_rate'])
    results['best_model'] = best_model

    return jsonify(results), 200

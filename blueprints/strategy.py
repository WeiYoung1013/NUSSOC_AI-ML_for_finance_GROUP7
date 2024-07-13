from flask import Blueprint, render_template, redirect, request, session, url_for
from extends import db
from models import UserModel, UserStockSelection
from LSTMforStocks import lstm_trading_strategy
from lightGBMforStocks import lightgbm_trading_strategy
from XGBoostforStocks import xgboost_trading_strategy


st = Blueprint('st', __name__,url_prefix="/strategy")

@st.route('', methods=['GET', 'POST'])
def strategy():
    stocks = [
        'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'BRK-A', 'BRK-B', 'JNJ', 'TSLA',
        'V', 'WMT', 'JPM', 'MA', 'PG', 'NVDA', 'HD', 'DIS', 'UNH', 'PYPL', 'BAC', 'INTC',
        'CMCSA', 'VZ', 'NFLX', 'PFE', 'ADBE', 'T', 'PEP', 'CRM', 'ABT', 'CSCO', 'ABBV',
        'XOM', 'AVGO', 'KO', 'CMG', 'AMD', 'DUK', 'QCOM', 'TMO', 'COST', 'LLY', 'NEE',
        'MRK', 'MDT', 'TMUS', 'ORCL', 'ACN', 'NKE', 'CL'
    ]
    if request.method == 'POST':
        selected_stocks = request.form.getlist('stocks')
        if len(selected_stocks) > 5:
            return redirect(url_for('strategy'))
        # 处理用户选择的股票逻辑
        else:
            selected_stocks_str = ','.join(selected_stocks)
            user_name = session['user_name']
            selection = UserStockSelection(user_name=user_name, stock_symbol=selected_stocks_str)
            db.session.add(selection)
            db.session.commit()
            session['selected_stocks'] = selected_stocks
            return redirect(url_for("st.show_results"))
    else:
        return render_template('strategy.html', stocks=stocks)
    
@st.route("/results")
def show_results():
    selected_stocks = session.get('selected_stocks')
    if not selected_stocks:
        return redirect(url_for('strategy'))

    # 调用策略分析函数
    lstm_return_rate, lstm_sharpe_ratio, lstm_alpha, lstm_beta, lstm_image_path = lstm_trading_strategy(tickers=selected_stocks)
    lightgbm_return_rate, lightgbm_sharpe_ratio, lightgbm_alpha, lightgbm_beta, lightgbm_image_path = lightgbm_trading_strategy(tickers=selected_stocks)
    xgboost_return_rate, xgboost_sharpe_ratio, xgboost_alpha, xgboost_beta, xgboost_image_path = xgboost_trading_strategy(tickers=selected_stocks)
    
    if(lstm_return_rate > lightgbm_return_rate and lstm_return_rate > xgboost_return_rate):
        return render_template('strategy_results.html',
                            best_model='LSTM',
                            best_return_rate=lstm_return_rate,
                            best_sharpe_ratio=lstm_sharpe_ratio,
                            best_alpha=lstm_alpha,
                            best_beta=lstm_beta,
                            best_image_path=lstm_image_path,
                            second_model='lightGBM',
                            second_return_rate=lightgbm_return_rate,
                            second_sharpe_ratio=lightgbm_sharpe_ratio,
                            second_alpha=lightgbm_alpha,
                            second_beta=lightgbm_beta,
                            second_image_path=lightgbm_image_path,
                            third_model='XGBoost',
                            third_return_rate=xgboost_return_rate,
                            third_sharpe_ratio=xgboost_sharpe_ratio,
                            third_alpha=xgboost_alpha,
                            third_beta=xgboost_beta,
                            third_image_path=xgboost_image_path)
    if(lightgbm_return_rate > lstm_return_rate and lightgbm_return_rate > xgboost_return_rate):
        return render_template('strategy_results.html',
                            best_model='lightGBM',
                            best_return_rate=lightgbm_return_rate,
                            best_sharpe_ratio=lightgbm_sharpe_ratio,
                            best_alpha=lightgbm_alpha,
                            best_beta=lightgbm_beta,
                            best_image_path=lightgbm_image_path,
                            second_model='LSTM',
                            second_return_rate=lstm_return_rate,
                            second_sharpe_ratio=lstm_sharpe_ratio,
                            second_alpha=lstm_alpha,
                            second_beta=lstm_beta,
                            second_image_path=lstm_image_path,
                            third_model='XGBoost',
                            third_return_rate=xgboost_return_rate,
                            third_sharpe_ratio=xgboost_sharpe_ratio,
                            third_alpha=xgboost_alpha,
                            third_beta=xgboost_beta,
                            third_image_path=xgboost_image_path)
    if(xgboost_return_rate > lstm_return_rate and xgboost_return_rate > lightgbm_return_rate):
        return render_template('strategy_results.html',
                            best_model='XGBoost',
                            best_return_rate=xgboost_return_rate,
                            best_sharpe_ratio=xgboost_sharpe_ratio,
                            best_alpha=xgboost_alpha,
                            best_beta=xgboost_beta,
                            best_image_path=xgboost_image_path,
                            second_model='LSTM',
                            second_return_rate=lstm_return_rate,
                            second_sharpe_ratio=lstm_sharpe_ratio,
                            second_alpha=lstm_alpha,
                            second_beta=lstm_beta,
                            second_image_path=lstm_image_path,
                            third_model='lightGBM',
                            third_return_rate=lightgbm_return_rate,
                            third_sharpe_ratio=lightgbm_sharpe_ratio,
                            third_alpha=lightgbm_alpha,
                            third_beta=lightgbm_beta,
                            third_image_path=lightgbm_image_path)

from flask import Blueprint, render_template, redirect, request, url_for

st = Blueprint('staticmethod', __name__,url_prefix="/strategy")

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
            return render_template('strategy.html', stocks=stocks, selected_stocks=selected_stocks)
    else:
        return render_template('strategy.html', stocks=stocks)
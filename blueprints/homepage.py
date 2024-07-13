from flask import Blueprint, render_template
from StockAnalyzer import StockAnalyzer
from extends import cache  # 导入缓存实例

hp = Blueprint('hp', __name__, url_prefix="/")

@hp.route('')
def homepage():
    data = cache.get('stock_data')
    if not data:
        data = get_stock_data()
        cache.set('stock_data', data, timeout=60*60)  # 缓存1小时
    return render_template('homepage.html', **data)

def get_stock_data():
    analyzer = StockAnalyzer()
    top_10_market_cap = analyzer.get_top_10_by_market_cap().to_dict(orient='records')
    top_10_growth_amount = analyzer.get_top_10_by_growth_amount().to_dict(orient='records')
    top_10_growth_rate = analyzer.get_top_10_by_growth_rate().to_dict(orient='records')
    data = {
        'top_10_market_cap': top_10_market_cap,
        'top_10_growth_amount': top_10_growth_amount,
        'top_10_growth_rate': top_10_growth_rate
    }
    return data

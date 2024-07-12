from flask import Blueprint, render_template
from StockAnalyzer import StockAnalyzer

hp = Blueprint('hp', __name__,url_prefix="/")


@hp.route('')
def homepage():
    analyzer = StockAnalyzer()
    top_10_market_cap = analyzer.get_top_10_by_market_cap().to_dict(orient='records')
    top_10_growth_amount = analyzer.get_top_10_by_growth_amount().to_dict(orient='records')
    top_10_growth_rate = analyzer.get_top_10_by_growth_rate().to_dict(orient='records')
    
    return render_template('homepage.html', 
                           top_10_market_cap=top_10_market_cap, 
                           top_10_growth_amount=top_10_growth_amount, 
                           top_10_growth_rate=top_10_growth_rate)
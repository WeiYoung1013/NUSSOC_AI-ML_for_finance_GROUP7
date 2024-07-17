from flask import Blueprint, jsonify
from StockAnalyzer import StockAnalyzer
from extends import cache  # 导入缓存实例

hp = Blueprint('hp', __name__, url_prefix="/")

# 定义自定义过滤器
def format_number(value):
    if isinstance(value, (float, int)):
        if value > 1e6:
            return f"{value:.2e}"  # 使用科学计数法
        return f"{value:.2f}"  # 保留两位小数
    return value

def format_percentage(value):
    if isinstance(value, (float, int)):
        return f"{value:.2%}"  # 转换为百分比格式
    return value

# 注册过滤器（这部分可以保留，但不影响REST API）
@hp.app_template_filter()
def scientific(value):
    return format_number(value)

@hp.app_template_filter()
def format_two_decimal(value):
    return format_number(value)

@hp.app_template_filter()
def percentage(value):
    return format_percentage(value)

@hp.route('', methods=['GET'])
def homepage():
    data = cache.get('stock_data')
    if not data:
        data = get_stock_data()
        cache.set('stock_data', data, timeout=60*60)  # 缓存1小时
    return data, 200  # 返回JSON响应

def get_stock_data():
    analyzer = StockAnalyzer()
    top_10_market_cap = analyzer.get_top_10_by_market_cap()
    top_10_growth_amount = analyzer.get_top_10_by_growth_amount()
    top_10_growth_rate = analyzer.get_top_10_by_growth_rate()
    data = {
        'top_10_market_cap': top_10_market_cap,
        'top_10_growth_amount': top_10_growth_amount,
        'top_10_growth_rate': top_10_growth_rate
    }
    return data

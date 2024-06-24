import yfinance as yf

def get_real_time_stock_price(stock_symbol):
    """
    Fetches the latest stock price for a given symbol.
    
    :param stock_symbol: Symbol of the stock (e.g., "HDFCBANK.NS" for HDFC Bank on NSE)
    :return: Latest closing price
    """
    stock = yf.Ticker(stock_symbol)
    hist = stock.history(period="1d")
    return hist['Close'].iloc[-1]

def get_real_time_index_value(index_symbol):
    """
    Fetches the latest index value for a given symbol.
    
    :param index_symbol: Symbol of the index (e.g., "^BSESN" for BSE SENSEX)
    :return: Latest closing value
    """
    index = yf.Ticker(index_symbol)
    hist = index.history(period="1d")
    return hist['Close'].iloc[-1]

# Example usage
print(get_real_time_stock_price("HDFCBANK.NS"))  # Use ".NS" for NSE stocks
print(get_real_time_index_value("^BSESN"))  # BSE SENSEX

import sqlite3

conn = sqlite3.connect('./database/database.db')


def fetch_stock_tickers():
    """
    Get all stocks on the database.
    Used to cache Combobox options.
    """
    try:
        with conn:
            cursor = conn.cursor()
            query = """SELECT ticker FROM stocks;"""
            cursor.execute(query)
            stocks = cursor.fetchall()

            return stocks

    except Exception as e:
        print(f'Could not fetch stock data due to {e}')

def get_stock_info(ticker, year):
    """
    Get data from a particular stock based on year
    """
    try:
        with conn:
            ticker = ticker.upper()

            cursor = conn.cursor()

            query = f"""SELECT 
                ticker,
                cnpj,
                razao_social,
                price_{year} FROM stocks WHERE ticker = '{ticker}'"""

            cursor.execute(query)

            stock = cursor.fetchone()

            if not stock:
                raise Exception(f'NÃO FOI POSSIVEL RESGATAR OS DADOS DA AÇÃO: {ticker}')
            else:
                return stock

    except Exception as e:
        print(f'Could not fetch stock data due to {e}')
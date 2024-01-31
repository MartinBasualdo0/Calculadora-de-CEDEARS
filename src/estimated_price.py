import locale
import pandas as pd
from src.tablas import get_main_table

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

def calculate_price(ticker:str, df:pd.DataFrame) -> str:
    ticker = ticker.upper()
    price = df.loc[df['tickers ARG'] == ticker, 'Tenés que comprar el cedear a $'].values[0]
    return f"El precio estimado debería ser: {locale.currency(price, grouping=True)}"
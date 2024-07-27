import pandas as pd
from src.tablas import get_main_table

def custom_currency_format(price: float) -> str:
    # Formatear el número con separador de miles y decimales personalizados
    formatted_price = f"{price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return formatted_price

def calculate_price(ticker: str, df: pd.DataFrame) -> str:
    ticker = ticker.upper()
    price = df.loc[df['tickers ARG'] == ticker, 'Tenés que comprar el cedear a $'].values[0]
    return f"El precio estimado debería ser: {custom_currency_format(price)}"
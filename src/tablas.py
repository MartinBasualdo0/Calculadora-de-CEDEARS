import pandas as pd
import yfinance as yf
from io import StringIO
from src.constants import COMAFI_URL, DICT_ORIGIN_CORREGIDOS, DICT_INTERNACIONALES_LOCALES


from src.scrap_config import get_legacy_session

def get_table_ratios():
    response = get_legacy_session().get(COMAFI_URL)
    html_content = response.text

    # Use pandas to read the HTML table content
    dfs = pd.read_html(StringIO(html_content))

    # dfs is a list of dataframes, one for each table found in the HTML content.
    # Assuming you want the first table:
    table = dfs[0]
    #Correcting some erroneus original tickers.
    table['Ticker  en  mercado  de  origen'] = table["Ticker  en  mercado  de  origen"].apply(lambda x: DICT_ORIGIN_CORREGIDOS[x] if x in DICT_ORIGIN_CORREGIDOS.keys() else x)
    return table

def calculate_ratio(ratio_str):
    # Split the string by ':' and convert parts to integers
    numerator, denominator = map(int, ratio_str.split(':'))
    # Perform the division
    return numerator / denominator

def get_main_table(CEDEARS: list[str]) -> pd.DataFrame:
    table_ratios = get_table_ratios()
    acciones_df = pd.DataFrame()
    DICT_LOCALES_INTERNACIONALES = {v: k for k, v in DICT_INTERNACIONALES_LOCALES.items()}
    for ticker in CEDEARS:
        ticker_ars = ticker + ".BA"
        if ticker in DICT_LOCALES_INTERNACIONALES.keys():
            ticker = DICT_LOCALES_INTERNACIONALES[ticker]
        #     ticker_ars += ".BA"
        # else:
        #     ticker_ars = ticker + ".BA"
        # try:
        tickers_data = {"tickers USA": ticker,
                        "tickers ARG": ticker_ars, #!
                        "cotizacion USA": yf.Ticker(ticker).info["currentPrice"],
                        "cotizacion ARG": yf.Ticker(ticker_ars).info["currentPrice"],
        }
        acciones_df = pd.concat([acciones_df, pd.DataFrame(tickers_data, index=[0])], ignore_index=True)
        # except Exception as e:
            # pass
        # print(acciones_df)
    acciones_df = acciones_df.merge(table_ratios[['Ratio  Cedear  /  valor  sub-yacente', 'Ticker  en  mercado  de  origen']], how="left", left_on="tickers USA", right_on='Ticker  en  mercado  de  origen')
    acciones_df = acciones_df.drop('Ticker  en  mercado  de  origen', axis=1)
    acciones_df['Ratio  Cedear  /  valor  sub-yacente'] = acciones_df['Ratio  Cedear  /  valor  sub-yacente'].apply(calculate_ratio)
    acciones_df["ccl cedear"] = (acciones_df["cotizacion ARG"] / acciones_df["cotizacion USA"] * acciones_df["Ratio  Cedear  /  valor  sub-yacente"]).round(2)
    acciones_df["ccl promedio"] = acciones_df["ccl cedear"].median()
    acciones_df["ccl promedio"] = acciones_df["ccl promedio"].round(2)
    acciones_df["Tenés que comprar el cedear a $"] = ((acciones_df["cotizacion USA"] * acciones_df["ccl promedio"]) / acciones_df["Ratio  Cedear  /  valor  sub-yacente"]).round(2)
    acciones_df = acciones_df.drop("tickers USA", axis=1)
    acciones_df["tickers ARG"] = acciones_df["tickers ARG"].str.replace(".BA", "")
    return acciones_df

def main_table(CEDEARS: list[str]):
    acciones_df = get_main_table(CEDEARS)
    return acciones_df

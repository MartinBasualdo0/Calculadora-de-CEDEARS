import pandas as pd
import yfinance as yf
from io import StringIO


from src.scrap_config import get_legacy_session

def get_table_ratios():
    response = get_legacy_session().get('https://www.comafi.com.ar/custodiaglobal/2483-Programas-Cedear.note.aspx')
    html_content = response.text

    # Use pandas to read the HTML table content
    dfs = pd.read_html(StringIO(html_content))

    # dfs is a list of dataframes, one for each table found in the HTML content.
    # Assuming you want the first table:
    table = dfs[0]
    return table

def calculate_ratio(ratio_str):
    # Split the string by ':' and convert parts to integers
    numerator, denominator = map(int, ratio_str.split(':'))
    # Perform the division
    return numerator / denominator

def get_main_table(CEDEARS: list[str]) -> pd.DataFrame:
    table_ratios = get_table_ratios()
    acciones_df = pd.DataFrame()
    for ticker in CEDEARS:
        try:
            tickers_data = {"tickers USA": ticker,
                            "tickers ARG": ticker + ".BA",
                            "cotizacion USA": yf.Ticker(ticker).info["currentPrice"],
                            "cotizacion ARG": yf.Ticker(ticker + ".BA" ).info["currentPrice"],
            }
            acciones_df = pd.concat([acciones_df, pd.DataFrame(tickers_data, index=[0])], ignore_index=True)
        except Exception as e:
            # print(f"An error occurred for ticker {ticker}: {e}")
            pass
    # acciones_df["tickers USA"] = CEDEARS
    # acciones_df["tickers ARG"] = acciones_df["tickers USA"] + ".BA"
    acciones_df = acciones_df.merge(table_ratios[['Ratio  Cedear  /  valor  sub-yacente', 'Ticker  en  mercado  de  origen']], how="left", left_on="tickers USA", right_on='Ticker  en  mercado  de  origen')
    acciones_df = acciones_df.drop('Ticker  en  mercado  de  origen', axis=1)
    acciones_df['Ratio  Cedear  /  valor  sub-yacente'] = acciones_df['Ratio  Cedear  /  valor  sub-yacente'].apply(calculate_ratio)
    # acciones_df["cotizacion USA"] = acciones_df["tickers USA"].apply(lambda x: yf.Ticker(x).info['currentPrice'])
    # acciones_df["cotizacion ARG"] = acciones_df["tickers ARG"].apply(lambda x: yf.Ticker(x).info['currentPrice'])
    acciones_df["ccl cedear"] = (acciones_df["cotizacion ARG"] / acciones_df["cotizacion USA"] * acciones_df["Ratio  Cedear  /  valor  sub-yacente"]).round(2)
    acciones_df["ccl promedio"] = acciones_df["ccl cedear"].median()
    acciones_df["ccl promedio"] = acciones_df["ccl promedio"].round(2)
    acciones_df["Tenés que comprar el cedear a $"] = ((acciones_df["cotizacion USA"] * acciones_df["ccl promedio"]) / acciones_df["Ratio  Cedear  /  valor  sub-yacente"]).round(2)
    acciones_df = acciones_df.drop("tickers ARG", axis=1)
    return acciones_df

def main_table(CEDEARS: list[str]):
    acciones_df = get_main_table(CEDEARS)
    return acciones_df

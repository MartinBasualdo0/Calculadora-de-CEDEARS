COMAFI_URL = 'https://www.comafi.com.ar/custodiaglobal/2483-Programas-Cedear.note.aspx'
CEDEARS_COMPLETO = ['MMM','ABT','ABBV','ANF','AGRO','ADS.DE','ADBE','AMD','AEG','AEM','BABA','GOOGL','MO','2600.HK','AMZN','ABEV','AMX','AAL','AXP','AIG','AMGN','ADI','AAPL','AMAT','ARCO','AZN','T','ADP','AVY','CAR','BIDU','BBVA','BBD','BSBR','SAN','BAC','BK','BCS','GOLD','BAS.DE','BAYN.DE','BRKB.VI','BHP','BIOX','BIIB','BB','BA','BP','LND','BAK','BRFS','BMY','AVGO','BG','CAH','CAT','CX','EBR','CVX','CBD','SBS','SID','CSCO','C','KO','KOF','CDE','COIN','CL','ELP','GLW','CAAP','COST','BN.PA','DE','DESP','DTEAF','DEO','DOCU','DOW','DD','EOAN.DE','EBAY','EA','LLY','AKO-B','ERJ','E','EFX','ERIC','ETSY','XOM','FNMA','FDX','FSLR','FMX','FMCC','FCX','GRMN','OGZPY','GE','GM','GPRK','GGB','GILD','GLOB','GFI','GS','PAC','ASR','TV','GSK','HAL','HOG','HMY','HDB','HL','HSY','HD','HNHPF','HMC','HON','HWM','HPQ','HSBC','IBN','INFY','ING','INTC','IP','IBM','IFF','ITUB','JD','JNJ','JCI','YY','JPM','KB','KMB','KGC','PHG','KEP','LRCX','LVS','LYG','LMT','LUKOY','MMC','MA','MCD','MDT','MELI','MBG.DE','MRK','META','MSFT','MUFG','MFG','MBT','MSI','NGG','NTCO','NEC1 GR','NTES','NFLX','NEM','NKE','NIO','NSANY','NOK','NMR','NG','NVS','NLMK','NUE','NVDA','ORCL','ORAN','PCAR','PAAS','PCRFY','PYPL','PSO','PEP','PBR','PFE','PSX','PBI','PKX','PG','QCOM','RTX','RIO','ROST','SHEL','CRM','005930.KS','SAP','SLB','SE','SHOP','SIEGY','SNAP','SNA','SNOW','SONY','SCCO','SPOT','SQ','SPGI','SBUX','SUZ','SYY','TSM','TGT','OAOFY','TIIAY','VIV','TEF','TS','TX','TSLA','TXN','TMO','TIMB','TTE','TM','TRV','TCOM','TRIP','TWLO','UGP','UL','UNP','X','UNH','URBN','USB','VALE','VRSN','VZ','V','VIST','VOD','WBA','WMT','DIS','WB','WFC','XRX','XP','YZCAY','YELP','ZM']
CEDEARS_SELECTOS = ["AAPL", "TSLA", "KO", "GOLD", "AMZN", "JPM", "NKE"]

#Para corregir algunos tickers internacionales
DICT_ORIGIN_CORREGIDOS = {
    'ADS': "ADS.DE",
    'AOCA': "2600.HK",
    "BAS GR" : "BAS.DE",
    "BAY GR": "BAYN.DE",
    "BRKB" : "BRKB.VI",
    "BSN GR":"BN.PA",
    "DTEA GR": "DTEAF",
    "EOAN GR": "EOAN.DE",
    "AKO.B": "AKO-B",
    "MBG GR": "MBG.DE",
    "MBT":"MTSS.ME",
    "SMSN LI" : "005930.KS",
    "VIST US": "VIST",
}

#Para corregir los cedears cuyos tickers varían de los internacionales
DICT_INTERNACIONALES_LOCALES = {
"ADS.DE": "ADS",
"2600.HK": "AOCA",
"BBVA": "BBV",
"BAC": "BA-C",
"BAS.DE" : "BAS",
"BAYN.DE": "BAYN",
"BRKB.VI": "BRKB",
#  "LND":"LND" #Todavía no se emitió,
#  "BAK":"BAK" Todavía no se emitió,
"BG":"BNG",
"CBR":"CBRD",
"KOF": "KOFM",
"BN.PA": "BSN",
#   "DTEAF": "DETEA", Parece que no cotiza,
"EOAN.DE": "EOAN",
# "AKOB":"AKOB",
# "FNMA":"FNMA",
# "FMCC":"FMCC",
# "OGZPY" : "OGZPY" #Gasprom
# "HNHPF": "HNHPF" # No cotiza
# "LUKOY": "LUKOY" #Rusia
"MBG.DE": "MBG",
"MTSS.ME":"MBT",
# "NEC1.F":"NEC1", Parece que no cotiza
# "NSANY": "NSAN",
"NOK": "NOKA",
# "NLMK.ME":"NLMK",
# "PCRFY":"PCRFY",
# "PSO": "PSO",
"PKX":"PKS",
# "005930.KS" : "SMSN",
#"OAOFY":"ATAD"
# TIIAY
"TEF":"TEFO",
"TS":"TEN",
"TX": "TXAR",
"TRV":"TRVV",
"VIST":"VIST",
"DIS":"DISN",
"WB": "WBK",
"XRX":"XROX",
# "YZCAY"
 }

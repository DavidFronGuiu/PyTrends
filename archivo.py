#pip install pytrends

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

# Máximo 5 terminos de búsqueda
kw_list = ["python", 
             "java", 
             "JavaScript", 
             "angular", 
             "C++"
           ]#Las mayúsculas no afectan

pytrends.build_payload(kw_list, 
                        cat=0, 
                        timeframe='today 12-m', 
                        geo='', 
                        gprop=''
                      )

iot = pytrends.interest_over_time()
iot.plot()
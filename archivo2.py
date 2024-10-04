from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

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
regionData = pytrends.interest_by_region(resolution='COUNTRY', 
                                          inc_low_vol=True, 
                                          inc_geo_code=False,
                                       )

#regionData[regionData['COUNTRY'] == 'Spain']

print(regionData)
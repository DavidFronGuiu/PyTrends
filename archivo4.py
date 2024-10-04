from pytrends.request import TrendReq
import numpy as np

# Inicializa pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Obtener las búsquedas trending para Estados Unidos
usTrending = pytrends.trending_searches(pn='united_states')

# Verificar si el DataFrame tiene datos
if not usTrending.empty:
    usTrending = usTrending.head(5)
    print("Trending searches DataFrame:")
    print(usTrending)

    # Convertir los valores del DataFrame a un array de NumPy
    trending_array = usTrending[0].values  # El DataFrame tiene una columna, que es el índice 0
    '''print("\nArray de búsquedas trending:")
    print(trending_array)'''

    kw_list = []
    for tema in trending_array:
        kw_list.append(tema)
    print(kw_list)
    
    pytrends.build_payload(kw_list, #Máximo 5 terminos
                            cat=0, 
                            timeframe='today 12-m', 
                            geo='', 
                            gprop=''
                        )
    
    iot = pytrends.interest_over_time()
    iot.plot()

else:
    print("No se encontraron datos de búsquedas trending.")

from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["python", "java", "JavaScript", "angular", "C++"]

# Obtener datos para España
pytrends.build_payload(kw_list, geo='ES')
interest_spain = pytrends.interest_over_time()

# Obtener datos para Portugal
pytrends.build_payload(kw_list, geo='PT')
interest_portugal = pytrends.interest_over_time()

# Eliminar la columna 'isPartial'
interest_spain = interest_spain.drop(columns=['isPartial'])
interest_portugal = interest_portugal.drop(columns=['isPartial'])

# Renombrar las columnas para incluir el país
interest_spain = interest_spain.rename(columns=lambda col: col + ' (Spain)')
interest_portugal = interest_portugal.rename(columns=lambda col: col + ' (Portugal)')

# Crear un DataFrame combinando España y Portugal en diferentes columnas
combined_df = pd.concat([interest_spain, interest_portugal], axis=1)

# Mostrar los datos combinados en un gráfico
combined_df.plot()
plt.title("Tendencias de búsqueda en España y Portugal")
plt.ylabel("Interés de búsqueda")
plt.xlabel("Fecha")
plt.xticks(rotation=45)
plt.legend(title="Palabras clave por país")
plt.tight_layout()
plt.show()
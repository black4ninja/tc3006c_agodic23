import serial  # conectar con python
import pandas as pd  # generar dataframes
import matplotlib.pyplot as plt # generar gráficas
from datetime import datetime  # obtener timestamp
from time import sleep

lectura = serial.Serial('/dev/ttyACM0', 9600) # conecta al puerto
sleep(3)

data = []
tiempo_medido = 10
temp_max = 60
temp_min = 10

#captura de datos
i = 0
while(i < tiempo_medido):
	arduino_data = lectura.readline()
	date = datetime.now(tz=None)
#	date = acotar a rangos deseables
	arduino_data = int(arduino_data)
#	arduino_data = pasar a grados centigrados

	if temp_max > arduino_data and arduino_data > temp_min:
		status = "optimal"
	else:
		status = "warning"
	data.append([arduino_data, date, status])
	i = i + 1

# generacion de dataframe
df = pd.DataFrame(data,columns =['temperature', 'date', 'status'])
df["temperature"].astype('int32')
df["date"] = pd.to_datetime(df["date"])
df["status"].astype('category')

print(df)

# escritura en archivo csv
df.to_csv("temp_i.csv")
df.to_csv("temp.csv",index=False)

# grafica la temperatura contra el tiempo
plt.plot(df["date"],df["temperature"])
plt.show()

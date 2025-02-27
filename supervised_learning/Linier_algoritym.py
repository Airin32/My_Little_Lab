import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('New Folder/Machine_Learning/Linier_regresion_algoritym/salaries.csv') # mengambil dataset bertipe csv dari file 
x = df.iloc[:,-2].values.reshape(-1,1) #memfilter data serta mengubah data dari tipe 1 dimensi ke 2 dimensi 
y = df.iloc[:,-1].values.reshape(-1,1) # untuk menggunakan fungsi Linier Regression
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0) # melatih data dan membuat data testing
model = LinearRegression() # memanggil class Linier Regresion
model.fit(x_train,y_train) # membuat Model data 
prediksi = model.predict([[2],[8],[4.5]]) # membuat prediksi data 
print("prediksi data : ",prediksi)
print("\n")
y_prediksi = model.predict(x_test) # Membuat prediksi data 
print(y_prediksi)
error = y_prediksi - y_test
print(error)
plt.scatter(x,y)
plt.plot(x_test,y_prediksi,'r')
plt.show()
r2 = r2_score(y_test,y_prediksi) # membuat score evaluasi data 
print(r2)
print(x_train)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score,accuracy_score
from sklearn import tree
import os 
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np
from sklearn.preprocessing import LabelEncoder

def get_data (filename) :
    if os.path.exists(filename) :
        data = pd.read_excel(filename)
        df = pd.DataFrame(data=data)
        return df 
    else :
        pd.DataFrame()
def Save_data (data,filename):
    df = pd.DataFrame(data=data)
    if os.path.exists(filename):
        df.to_excel(filename,mode='a',index=False,header=False)
    else :
        df.to_excel(filename,index=False,header=False)


class Predictor :
    def __init__ (self,data):
        self.__data = data 
        self.__profit_data = None 
        self.__sales_data = None 
    
    def compresor_data (self,dolar) :
        return dolar * (100/10000)    
    
    @property
    def get_data (self) :  
        data = self.__data 
        data = pd.DataFrame(data=data)
        profit = np.array(data.iloc[:,0]).reshape(1,-1)
        sales = np.array(data.iloc[:,1]).reshape(1,-1)
        profit = profit[0]
        sales = sales[0]
        data_pf = []
        data_sales = []
        for i in range(len(profit)) :
            data_change = self.compresor_data(profit[i])
            data_sls_change = self.compresor_data(sales[i])
            data_pf.append(data_change)
            data_sales.append(data_sls_change)
        profit = np.array(data_pf)
        sales = np.array(data_sales)
        range_data_profit = np.array([profit[i] / 7.057 for i in range(len(profit))])
        range_data_sales = np.array([sales[i] / 7.057 for i in range(len(sales))])
        self.__profit_data = profit
        self.__sales_data = sales
        return self.__profit_data,self.__sales_data,range_data_profit,range_data_sales
    
    def Main_Predictor (self) :
        profit,sales,range_profit,range_sales = self.get_data
        random_data_profit = np.array([np.random.randint(min(profit),max(profit)) / 7.057 for i in range(len(profit))]).reshape(-1,1)
        random_data_sales = np.array([np.random.randint(min(sales),max(sales)) / 7.057 for i in range(len(sales))]).reshape(-1,1)
        y_profit = profit.reshape(-1,1)
        x_profit = range_profit.reshape(-1,1)
        y_sales = sales.reshape(-1,1)
        x_sales = range_sales.reshape(-1,1)
        Label_profit = []
        Label_sales = []
        x_train_pf,x_test_pf,y_train_pf,y_test_pf = train_test_split(x_profit,y_profit,test_size=0.25, random_state=5)
        x_train_sls,x_test_sls,y_train_sls,y_test_sls = train_test_split(x_sales,y_sales,test_size=0.25,random_state=6)
        model_profit = LinearRegression()
        model_sales = LinearRegression()
        model_profit.fit(x_train_pf,y_train_pf)
        model_sales.fit(x_train_sls,y_train_sls)
        predict_profit = model_profit.predict(random_data_profit)
        predict_sales = model_sales.predict(random_data_sales)
        predict_profit = np.array(predict_profit).reshape(1,-1)
        predict_sales = np.array(predict_sales).reshape(1,-1)
        predict_profit = predict_profit[0]
        predict_sales = predict_sales[0]
        for i in range(len(predict_profit)) :
            if predict_profit[i] >= 50 :
                Label_profit.append(1)
            else :
                Label_profit.append(0)
        for i in range(len(predict_sales)) :
            if predict_sales[i] >= 50 :
                Label_sales.append(1)
            else :
                Label_sales.append(0)
        random_data_profit = random_data_profit.reshape(1,-1)
        random_data_sales = random_data_sales.reshape(1,-1)
        random_data_profit = random_data_profit[0]
        random_data_sales = random_data_sales[0]
        d_profit = {
            'Predict_Profit' : predict_profit,
            'Rentang_data_Profit' : random_data_profit,
            'Label_Profit' : Label_profit
        }
        d_sales = {
            'Predict_Sales' : predict_sales,
            'Rentang_data_Sales' : random_data_sales,
            'Label_Sales' : Label_sales 
        }
        data_frame_profit = pd.DataFrame(data=d_profit)
        data_frame_sales = pd.DataFrame(data=d_sales)
        return data_frame_profit,data_frame_sales
    

class Basic_classifier :
    def __init__ (self,data_profit,data_sales):
        self.__data_profit = data_profit
        self.__data_sales = data_sales 
        self.__train_data = get_data('train_data.xlsx')
    
    @property
    def get_train (self) :
        d_set = self.__train_data
        dataframe = pd.DataFrame(data=d_set)
        return dataframe
    
    @property
    def get_profit_data (self) :
        data = self.__data_profit
        data = pd.DataFrame(data=data)
        predict_data = data.iloc[:,0].values.reshape(-1,1)
        rentang_data = data.iloc[:,1].values.reshape(-1,1)
        true_false = data.iloc[:,2].values.reshape(-1,1)
        return predict_data,rentang_data,true_false
    
    @property 
    def get_sales_data (self) :
        data = self.__data_sales 
        data = pd.DataFrame(data=data)
        predict_data = data.iloc[:,0].values.reshape(-1,1)
        rentang_data = data.iloc[:,1].values.reshape(-1,1)
        true_false = data.iloc[:,2].values.reshape(-1,1)
        return predict_data,rentang_data,true_false
    
    def Labels_writter (self,Data_array) :
        Condition_labels = []
        for i in range(len(Data_array)) :
            if Data_array[i] == 1 :
                Condition_labels.append('Good_condition')
            else :
                Condition_labels.append('Bad_condition')
        return Condition_labels
    
    def profit_data_classifier (self) :
        actual_data,range_data,true_false_data = self.get_profit_data
        train_data = self.get_train
        df_train_data = pd.DataFrame(data=train_data)
        x = df_train_data.iloc[:,0].values.reshape(-1,1)
        y = df_train_data.iloc[:,2].values.reshape(-1,1)
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=25)
        model = LogisticRegression()
        model.fit(x_train,y_train)    
        real_predict = model.predict(actual_data)
        real_predict = np.array(real_predict).reshape(1,-1)
        range_data = np.array(range_data).reshape(1,-1)
        true_false_data = np.array(true_false_data).reshape(1,-1)
        real_predict = real_predict[0]
        range_data = range_data[0]
        true_false_data = true_false_data[0]
        true_false_data = self.Labels_writter(real_predict)
        actual_data = np.array(actual_data).reshape(1,-1)
        actual_data = actual_data[0]
        d_frame = {
            'Data' : actual_data,
            'range_data' : range_data,
            'Condition' : true_false_data
        }
        dataframe = pd.DataFrame(d_frame)
        return dataframe

    def sales_data_classifier (self) :
        actual_data,range_data,true_false_data = self.get_sales_data
        train_data = self.get_train
        d_frame_train = pd.DataFrame(data=train_data)
        x = d_frame_train.iloc[:,1].values.reshape(-1,1)
        y = d_frame_train.iloc[:,2].values.reshape(-1,1)
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=25)
        model = LogisticRegression()
        model.fit(x_train,y_train)
        real_predict = model.predict(actual_data)
        real_predict = np.array(real_predict).reshape(1,-1)
        range_data = np.array(range_data).reshape(1,-1)
        range_data = range_data[0]
        real_predict = real_predict[0]
        true_false_data = self.Labels_writter(real_predict)
        actual_data = np.array(actual_data).reshape(1,-1)
        actual_data = actual_data[0]
        d_set = {
            'Data' : actual_data,
            'range_data' : range_data,
            'Condition' : true_false_data
        }
        dataframe = pd.DataFrame(data=d_set)
        return dataframe

class Advance_clasicfier_classifier :
    def __init__ (self,Data) :
        self.__data = Data 
        self.__traindata = get_data('Decision_tree_train.xlsx')

    @property
    def get_train (self):
        data_train = self.__traindata
        data_train = pd.DataFrame(data=data_train)
        Avarage = np.array(data_train.iloc[:,6])
        x = data_train.copy()
        labels = []
        for i in range(len(Avarage)):
            if Avarage[i] >= 50 :
                labels.append(1)
            else :
                labels.append(0)
        y = np.array(labels)
        return x,y
    
    @property 
    def get_data_profit (self) :
        actual_data = self.__data
        actual_data = pd.DataFrame(data=actual_data)
        profit_data = np.array(actual_data.iloc[:,0])
        range_profit = np.array(actual_data.iloc[:,1])
        return profit_data,range_profit

    @property
    def get_data_sales (self) :
        actual_data = self.__data
        actual_data = pd.DataFrame(data=actual_data)
        sales_data = np.array(actual_data.iloc[:,3])
        rentang_sales = np.array(actual_data.iloc[:,4])
        return sales_data,rentang_sales
    
    def Main_classification (self):
        data_profit,rentang_profit = self.get_data_profit
        data_sales,rentang_sales = self.get_data_sales
        data_target = self.__data
        data_target = pd.DataFrame(data=data_target)
        data_profit = data_target.iloc[:,0]
        data_sales = data_target.iloc[:,3]
        Avarage = []
        for i in range(len(data_profit)):
            data = (data_profit[i] + data_sales[i] ) * 0.5
            Avarage.append(data)
        Avarage = {'Avarage' : Avarage}
        Avarage = pd.DataFrame(data=Avarage)
        data_target = pd.concat([data_target,Avarage],axis=1)
        x,y = self.get_train
        y = y.reshape(-1,1)
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=5)
        model = DecisionTreeClassifier()
        model.fit(x_train,y_train)
        predict = model.predict(data_target)
        predict = np.array(predict).reshape(1,-1)
        predict = predict[0]
        true_false = []
        for i in range(len(predict)) :
            if predict[i] == 1:
                true_false.append('Good Condition')
            else :
                true_false.append('Bad Condition')
        d_frame = {
            'Predict_profit' : data_profit,
            'Rentang_data_profit' : rentang_profit,
            'Predict_sales' : data_sales,
            'Ranteng_data_sales' : rentang_sales,
            'Condition' : true_false
        }
        data_frame = pd.DataFrame(data=d_frame)
        return data_frame

class compleks_classifire_Regresor :
    def __init__ (self,data) :
        self.__data = data 
        self.__train_data = get_data('Train_data_Random_Forest_Regresor.xlsx')
    
    @property
    def get_train_data (self) :
        data = self.__train_data
        data = pd.DataFrame(data=data)
        Categori = np.array(["data profit","data sales","Kepuasan"])
        enc = LabelEncoder()
        enc.fit(Categori)
        data['Jenis_data'] = enc.transform(data['Jenis_data'])
        actual_data = data.drop(['Target'],axis=1)
        Target = data['Target']
        return actual_data.values,Target.values
    
    @property
    def get_data (self) :
        data = self.__data 
        data = pd.DataFrame(data=data)
        Categori = np.array(["data profit","data sales","Kepuasan"])
        enc = LabelEncoder()
        enc.fit(Categori)
        data['Jenis_data'] = enc.transform(data['Jenis_data'])
        return data.values

    def Main_Classification (self):
        x,y = self.get_train_data
        data = self.get_data
        getdata = self.__data
        getdata = pd.DataFrame(data=getdata)
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=4)
        model = RandomForestRegressor()
        model.fit(x_train,y_train)
        prediction = model.predict(data)
        evaluasi = []
        for i in range(len(prediction)) :
            if prediction[i] < 0.5 :
                evaluasi.append("Bad Condition")
            elif prediction[i] == 0.5 :
                evaluasi.append("Litte Bad Condition")
            elif prediction[i] == 0.75 :
                evaluasi.append("Little Good Condition")
            else :
                evaluasi.append("Good Condition")
        d = {'Condition' : evaluasi}
        d = pd.DataFrame(data=d)
        data_frame = pd.concat([getdata,d],axis=1)
        return data_frame
    
class
data_testing = get_data('Testing_file.xlsx')
testing_random = compleks_classifire_Regresor(data=data_testing)
data = testing_random.Main_Classification()
Save_data(data,'Result_testing.xlsx')

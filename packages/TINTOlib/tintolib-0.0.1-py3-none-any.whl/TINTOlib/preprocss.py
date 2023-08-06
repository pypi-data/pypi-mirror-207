
from refined import REFINED
from  barGraph import BarGraph
import  pandas as pd
from sklearn.preprocessing import MinMaxScaler


datapath="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\Datasets\\graph\\c.csv"
respath="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\Datasets\\cancer.csv"
data=pd.read_csv(datapath).values
scaler = MinMaxScaler()
X = data[:, :-1]
X= X[:, 1:] #delete

Y= pd.DataFrame(data[:, -1])

data_norm =pd.DataFrame( scaler.fit_transform(X))

df=pd.concat([data_norm,Y],axis=1)
print(data_norm)
df.to_csv(respath,index=False)

"""
model=BarGraph(verbose=False,problem="supervised")
data="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\Datasets\\cancer.csv"
folder="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\ResultadosEjemplos\\Combination"

model.generateImages(data, folder)
"""
"""
Crea un algoritmo que dada una matriz de dimension MxM, una matriz con 
"""
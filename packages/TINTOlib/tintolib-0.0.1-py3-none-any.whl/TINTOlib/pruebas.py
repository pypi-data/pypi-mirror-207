
from refined import REFINED
from  barGraph import BarGraph
from distanceMatrix import  DistanceMatrix
from combination import Combination
from igtd import IGTD

data="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\Datasets\\cancer.csv"

folder_name="IGTD"
#Supervised
model=IGTD(verbose=False,problem="supervised")
folder="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\ResultadosEjemplos\\"+folder_name+"\\Supervised"
model.generateImages(data, folder)

#Unsupervised
model=IGTD(verbose=False,problem="unsupervised")
folder="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\ResultadosEjemplos\\"+folder_name+"\\Unsupervised"
model.generateImages(data, folder)

#Regression
model=IGTD(verbose=False,problem="regression")
folder="C:\\Users\\Borja\\PycharmProjects\\TINTORERA\\ResultadosEjemplos\\"+folder_name+"\\Regression"
model.generateImages(data, folder)
"""
Crea un algoritmo que dada una matriz de dimension MxM, una matriz con 
"""
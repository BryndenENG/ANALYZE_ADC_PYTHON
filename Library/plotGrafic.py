###############################################################################
#IMPORT

import Library.importDATA as id


import os
import pandas as pd
import matplotlib.pyplot as plt

###############################################################################
def plotGF(maindir:str)->list :
     'Graphic plot of the respective equipment'
     'maindir: script execution directory'
     'equipment: equipment that will print the data of your registrars'


     address1 = maindir + '\\DADOS\\DADOS_GAIN'
     address2 = maindir + '\\DADOS\\DADOS_OFFSET'

     dir1 = os.listdir(address1)
     dir2 = os.listdir(address2)

     ad1 = []
     ad2 = []
     for x in dir1:
          ad1.append(address1 +'//'+x)
     for x in dir2:
          ad2.append(address2 +'//'+x)

     dataFrameGCC = csvToSeriesPandas(ad1, 'gain')
     dataFrameOCC = csvToSeriesPandas(ad2, 'offset')

     y1 = []
     y2 = []


     y1 = slicing(dataFrameGCC)
     y2 = slicing(dataFrameOCC)
     labels = generateLabels()

     equipament = 1
     for x in range(len(y1)):
          fig, axs = plt.subplots(2,3, figsize=(300,20))

          axs[0,0].bar(labels,y1[x][0])
          axs[0,0].set_title('GCC0')
          axs[0,1].bar(labels,y1[x][1])
          axs[0,1].set_title('GCC1')
          axs[0,2].bar(labels,y1[x][2])
          axs[0,2].set_title('GCC2')

          axs[1,0].bar(labels,y2[x][0])
          axs[1,0].set_title('OCC0')
          axs[1,1].bar(labels,y2[x][1])
          axs[1,1].set_title('OCC1')
          axs[1,2].bar(labels,y2[x][2])
          axs[1,2].set_title('OCC2')
         
          name = 'Equipament' + str(equipament)
          fig.suptitle(name)
          plt.show()
          name += '.png'
          fig.savefig(name)
          equipament += 1
     
     resultado = sumDF(y1,y2)

     fig, axs = plt.subplots(2,3, figsize=(300,20))
     axs[0,0].bar(labels,resultado[0]['SUM'])
     axs[0,0].set_title('GCC0')
     axs[0,1].bar(labels,resultado[1]['SUM'])
     axs[0,0].set_title('GCC1')
     axs[0,2].bar(labels,resultado[2]['SUM'])
     axs[0,0].set_title('GCC2')
     axs[1,0].bar(labels,resultado[3]['SUM'])
     axs[0,0].set_title('OCC0')
     axs[1,1].bar(labels,resultado[4]['SUM'])
     axs[0,0].set_title('OCC1')
     axs[1,2].bar(labels,resultado[5]['SUM'])
     axs[0,0].set_title('OCC2')
     name = 'SOMATÓRIO'
     fig.suptitle(name)
     plt.show()
     name += '.png'
     fig.savefig(name)

     resultado[0].to_csv("GCC0_TOTAL.csv")
     resultado[1].to_csv("GCC1_TOTAL.csv")
     resultado[2].to_csv("GCC2_TOTAL.csv")
     resultado[3].to_csv("OCC0_TOTAL.csv")
     resultado[4].to_csv("OCC1_TOTAL.csv")
     resultado[5].to_csv("OCC2_TOTAL.csv")

     return resultado

###############################################################################
def csvToSeriesPandas(address:list, typedata:str)->list:
     aux0 = 0
     aux1 = []
     dataFrameR = []
     for x in address:
          if typedata == 'gain':
               if aux0 == 0:
                    aux1.append(id.csvToDataFrame(x, 'GCC0'))
               if aux0 == 1:
                    aux1.append(id.csvToDataFrame(x, 'GCC1'))
               if aux0 == 2:
                    aux1.append(id.csvToDataFrame(x, 'GCC2'))
          else:
               if aux0 == 0:
                    aux1.append(id.csvToDataFrame(x, 'OCC0'))
               if aux0 == 1:
                    aux1.append(id.csvToDataFrame(x, 'OCC0'))
               if aux0 == 2:
                    aux1.append(id.csvToDataFrame(x, 'OCC0'))
          aux0 += 1
          if aux0 == 3:
               dataFrameR.append(aux1)
               aux0 = 0
               aux1 = []
     
     return dataFrameR
###############################################################################
def slicing(data:list)->list:
     a = []
     for x in data:
          z = []
          for y in x:
               z.append(y['Frequency'])
          a.append(z)
     return a
###############################################################################
def generateLabels()->list:
     a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
     w = []
     for x in a:
          for y in a:
               w.append("0x" + x + y)
     return w
###############################################################################
def sumDF(list1:list,list2:list)->list:

     GCC0 = pd.DataFrame()
     GCC1 = pd.DataFrame()
     GCC2 = pd.DataFrame()
     OCC0 = pd.DataFrame()
     OCC1 = pd.DataFrame()
     OCC2 = pd.DataFrame()

     for a in range(len(list1)):

          GCC0['GCC0_EQ'+str(a)] = list1[a][0]
          GCC1['GCC1_EQ'+str(a)] = list1[a][1]
          GCC2['GCC2_EQ'+str(a)] = list1[a][2]

          OCC0['OCC0_EQ'+str(a)] = list2[a][0]
          OCC1['OCC1_EQ'+str(a)] = list2[a][1]
          OCC2['OCC2_EQ'+str(a)] = list2[a][2]
          

     GCC0['SUM'] =  GCC0.sum(axis = 1)
     GCC1['SUM'] =  GCC1.sum(axis = 1)
     GCC2['SUM'] =  GCC2.sum(axis = 1)
     OCC0['SUM'] =  OCC0.sum(axis = 1)
     OCC1['SUM'] =  OCC1.sum(axis = 1)
     OCC2['SUM'] =  OCC2.sum(axis = 1)

     result = []
     result.append(GCC0)
     result.append(GCC1)
     result.append(GCC2)
     result.append(OCC0)
     result.append(OCC1)
     result.append(OCC2)

     return result
###############################################################################
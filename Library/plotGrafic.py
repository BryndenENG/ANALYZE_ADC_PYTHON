###############################################################################
#IMPORT

import Library.importDATA as id


import os
import pandas as pd
import matplotlib.pyplot as plt

###############################################################################
def plotGF(maindir:str):
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
          fig, axs = plt.subplots(6,1, figsize=(300,20))

          axs[0].bar(labels,y1[x][0])
          axs[0].set_title('GCC0')
          axs[1].bar(labels,y1[x][1])
          axs[1].set_title('GCC1')
          axs[2].bar(labels,y1[x][2])
          axs[2].set_title('GCC2')

          axs[3].bar(labels,y2[x][0])
          axs[3].set_title('OCC0')
          axs[4].bar(labels,y2[x][1])
          axs[4].set_title('OCC1')
          axs[5].bar(labels,y2[x][2])
          axs[5].set_title('OCC2')
         
          name = 'Equipament' + str(equipament)
          fig.suptitle(name)
          plt.show()
          name += '.png'
          fig.savefig(name)
          equipament += 1
     
     

    


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


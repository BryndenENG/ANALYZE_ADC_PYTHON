###############################################################################
#IMPORT
import pandas as pd
import numpy  as np
###############################################################################
def organizeDataFrame(dados0:list, nameColumn0:list, 
                      dados1:list,nameColumn1:list):

     'Filtering dataframe, organizing calibration data in three columns'
     x = organizeData(dados0, nameColumn0)
     y = organizeData(dados1, nameColumn1)
     
     return x, y

###############################################################################

def organizeData(dados:list,nameColumn:list)->list:
     'Returns a list of items with data type panda organized in 3 columns'
     dataFRAME = []
     for x in dados:
          a = 0
          b = []
          c = []
          d = []
          for i, row in x.iterrows():
               if a == 0:
                    b.append(row['MISO'])
               elif a == 1:
                    c.append(row['MISO'])
               elif a == 2:
                    d.append(row['MISO'])
                    
               if a < 2:
                    a += 1
               else:
                    a = 0

          data = []
          data.append(np.array(b))
          data.append(np.array(c))
          data.append(np.array(d))
          data = np.array(data)
          data = data.T

          index = []
          for i in range(len(b)):
               index.append(i)
          dataFRAME.append(pd.DataFrame(data,index, columns=[nameColumn]))
     
     return dataFRAME

###############################################################################









###############################################################################
#IMPORT
import pandas as pd
###############################################################################

###############################################################################
def countValue(df1:list,df2:list):
     'Performs the frequency of the received data def1 refers to the gain' 
     'values def2 refers to the offset values'
     val1 = count(df1,'gain')
     val2 = count(df2, 'offset')

     return val1, val2

###############################################################################
def count(df:list, dado:str):
     'Performs the count and names the columns according to the value inserted'
     'in the dados string'
     countValue = []
     for x in df:
          aux = []
          for y in range(3):
               if y == 0:
                    filtroCount = 0
                    if dado == 'gain':
                         filtroCount = auxCount0(x,'GCC0')
                    else:
                         filtroCount = auxCount0(x,'OCC0')
                    aux.append(filtroCount)
               elif y == 1:
                    if dado == 'gain':
                         filtroCount = auxCount0(x,'GCC1')
                    else:
                         filtroCount = auxCount0(x,'OCC1')
                    aux.append(filtroCount)
               elif y == 2:
                    if dado == 'gain':
                         filtroCount = auxCount0(x,'GCC2')
                    else:
                         filtroCount = auxCount0(x,'OCC2')
                    aux.append(filtroCount)
          countValue.append(aux)
     
     return countValue

###############################################################################
def auxCount0(x, string:str):
     
     filtro = (x.filter(like=string)).value_counts(ascending = False).reset_index()
     filtro.columns = [string, 'FREQUENCIA']
     return filtro

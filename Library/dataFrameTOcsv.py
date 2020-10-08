###############################################################################
#IMPORT
from Library import moveData as md

import pandas as pd

###############################################################################
def convertCSV(lista1:list, typeVal1:str, lista2:list, typeVal2:str, addressDir: str):
     pandasCSV(lista1, typeVal1)
     pandasCSV(lista2, typeVal2)
     md.moveDataCSV(addressDir)

###############################################################################
def pandasCSV(lista:list, typeVal:str):

     aux0 = 0
     namecsv = ''
     for x in lista:
          aux1 = 0
          for y in x:
               if aux1 == 0:
                    if typeVal == 'gain':
                         namecsv = 'Equipamento_'+ str(aux0) + '_GCC0' + '.csv'
                         y.to_csv(namecsv)
                    elif typeVal == 'offset':
                         namecsv = 'Equipamento_'+ str(aux0) + '_OCC0' + '.csv'
                         y.to_csv(namecsv)
               elif aux1 == 1:
                    if typeVal == 'gain':
                         namecsv = 'Equipamento_'+ str(aux0) + '_GCC1' + '.csv'
                         y.to_csv(namecsv)
                    elif typeVal == 'offset':
                         namecsv = 'Equipamento_'+ str(aux0) + '_OCC1' + '.csv'
                         y.to_csv(namecsv)
               if aux1 == 2:
                    if typeVal == 'gain':
                         namecsv = 'Equipamento_'+ str(aux0) + '_GCC2' + '.csv'
                         y.to_csv(namecsv)
                    elif typeVal == 'offset':
                         namecsv = 'Equipamento_'+ str(aux0) + '_OCC2' + '.csv'
                         y.to_csv(namecsv)
               aux1 += 1
          
          aux0 += 1
###############################################################################


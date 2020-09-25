###############################################################################
#-O PROGRAMA VISA A ANÁLISE DOS DADOS COLETADOS DE CALIBRAÇÃO, EFETUANDO:
#    SEPARAÇÃO DOS DADOS;
#    ANÁLISE DAS INFORMAÇÕES.
###############################################################################
# IMPORT
from Library.countValue import count
import Library.returnMainDir as rd
import Library.createDir     as cd
import Library.moveData      as md
import Library.importDATA    as iD
import Library.organizeData  as od
import Library.countValue    as cv

import pandas as pl
############################################################################### 
# FUNCTION


##############################################################################

# Creates directories to store data provided and files with refined data
addressDir = rd.pastaFiles()
cd.createDir(addressDir)

# Moves calibration files to DADOS folder
print('#########################################################################')
print('OS ARQUIVOS DA PASTA DADOS SERÃO EXCLUIDOS, SE DESEJAR MANTE-LOS COPIE-OS')
print('CASO CONTRÁRIO OS MESMOS SERÃO EXCLUIDOS!')
print('#########################################################################')
input('PRESSIONE ENTER PARA CONTINUAR... ')
md.moveData(addressDir)

# Imports data from the DATA folder in csv format
dataGain, dataOffset = iD.importDATA(addressDir)

title0 = ['GCC0','GCC1','GCC2']
title1 = ['OCC0','OCC1','OCC2']
gain, offset = od.organizeDataFrame(dataGain, title0, dataOffset, title1)

countGain, countOffset = cv.countValue(gain, offset)

print(countGain)
print('---')
print(countOffset)


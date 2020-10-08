###############################################################################
#-O PROGRAMA VISA A ANÁLISE DOS DADOS COLETADOS DE CALIBRAÇÃO, EFETUANDO:
#    SEPARAÇÃO DOS DADOS;
#    ANÁLISE DAS INFORMAÇÕES.
###############################################################################
# IMPORT
from Library.countValue import count
import Library.returnMainDir  as rd
import Library.createDir      as cd
import Library.moveData       as md
import Library.importDATA     as iD
import Library.organizeData   as od
import Library.countValue     as cv
import Library.dataFrameTOcsv as tscv
import Library.plotGrafic     as pg

import pandas as pl
##############################################################################

# Indicates the directory in which the script is being executed
addressDir = rd.pastaFiles()
# Creates directories to store data provided and files with refined data
cd.createDir(addressDir)

# User warning message in Portuguese
print('#########################################################################')
print('OS ARQUIVOS DA PASTA DADOS SERÃO EXCLUIDOS, SE DESEJAR MANTE-LOS COPIE-OS')
print('CASO CONTRÁRIO OS MESMOS SERÃO EXCLUIDOS!')
print('#########################################################################')
input('PRESSIONE ENTER PARA CONTINUAR... ')

# Moves calibration files to DADOS folder
md.moveData(addressDir)

# Imports data from the DATA folder in csv format
dataGain, dataOffset = iD.importDATA(addressDir)

# Organizes data for later counting
title0 = ['GCC0','GCC1','GCC2']
title1 = ['OCC0','OCC1','OCC2']
gain, offset = od.organizeDataFrame(dataGain, title0, dataOffset, title1)

# Performs the counting of data frequency in each of the 6 registers (3 of 
#gains and 3 of offset)
countGain, countOffset = cv.countValue(gain, offset)

# Converts the Series.Pandas in csv format to the DADOS_GAIN and DADOS_OFFSET
#subdirectories
tscv.convertCSV(countGain, 'gain', countOffset, 'offset', addressDir)

# Criar uma função com o propósito de plotar o gráfico para cada equipamento
#essa função plotará os 6 gráficos GCC0, GCC1, GCC2, OCC0, OCC1 E OCC2.
#    Deverá ser criado uma função para coletar o dado em csv
pg.plotGF(addressDir)


# Criar uma função que somará todos os dados de todos os registradores dos 
#equipamentos e em seguida gerar um gráfico geral respectivo a todos 
#equipamentos 
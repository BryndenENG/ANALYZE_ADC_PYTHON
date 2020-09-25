###############################################################################
#IMPORT
import os
import shutil
###############################################################################

def moveData(diretory: str)->None:
     'Change directory of calibration files'

     #List all files and directories in the current directory
     a = os.listdir(diretory)
     
     #Extract only files with '.txt' format which store the calibration files
     filesDATA = []
     for x in a:
          if '.csv' in x or '.txt' in x:
               b = diretory + "\\" + x
               filesDATA.append(b)

     #Changes the directory of the '.txt' and '.csv' files to the DADOS subdirectory
     #Clears the directory if you already have a file
     diretory += '\\DADOS'
     a = os.listdir(diretory)
     for x in a:
          if '.csv' in x or '.txt' in x:
               b = diretory + '\\' + x
               os.remove(b)

     for x in filesDATA:
          shutil.move(x,diretory)

###############################################################################
#Test
#moveData(r'C:\Users\tarci\OneDrive\Área de Trabalho\Trabalho\AEPH\DADOS DE CALIBRAÇÃO\ANALISE PY')

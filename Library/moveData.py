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
def moveDataCSV(diretory: str):
     
     #List all files and directories in the current directory
     a = os.listdir(diretory)

     #Extract only files with '.txt' format which store the calibration files
     filesDATA1 = []
     filesDATA2 = []
     for x in a:
          if '.csv' in x or '.txt' in x:
               if 'GCC' in x:
                    b = diretory + "\\" + x
                    filesDATA1.append(b)
               elif 'OCC' in x:
                    b = diretory + "\\" + x
                    filesDATA2.append(b)
     
     #Changes the directory of the '.txt' and '.csv' files to the DADOS subdirectory
     #Clears the directory if you already have a file
     diretory1 = diretory + '\\DADOS\\DADOS_GAIN'
     diretory2 = diretory + '\\DADOS\\DADOS_OFFSET'
     a = os.listdir(diretory1)
     b = os.listdir(diretory2)

     # System Message
     print()
     print('#########################################################################')
     print("OS SUBDIRETÓRIOS DATA_GAIN E DATA_OFFSET TERÃO SEU CONTEÚDO DELETADO,")
     print("CASO DESEJE PRESERVA-LOS EFETUE UMA CÓPIA ANTES DE PROSSEGUIR!")
     print('#########################################################################')
     input('PRESSIONE ENTER PARA CONTINUAR...')
     print()


     for x in a:
          y = diretory1 + '\\' + x
          os.remove(y)
     for x in b:
          y = diretory2 + '\\' + x
          os.remove(y)

     for x in filesDATA1:
          shutil.move(x,diretory1)
     for x in filesDATA2:
          shutil.move(x,diretory2)

###############################################################################
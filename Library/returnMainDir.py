###############################################################################
#IMPORT
import os
###############################################################################

def pastaFiles() -> str:
     'returns the directory of the folder in which the script is being executed'

     #-Returns current directory address and breaks each part of the address 
     #based on '\' (windows default)
     enderecoSplit = os.getcwd().split('\\')
     
     #Setting the address for manipulation
     endereco = ''
     for x in enderecoSplit:
          endereco += x + '\\'
     lenEndereco = len(endereco)
     endereco = endereco[:lenEndereco-1]
     
     return endereco
###############################################################################
#IMPORT
import os

###############################################################################
def createDir(diretory:str):
     'creates the referring usage directories for the script'
     dirDADOS = 0
     DirGain = 0
     DirOffset = 0
     # Strings for deleting and creating directories
     dirMainData = diretory + '\\DADOS'
     dirGain     = dirMainData + '\\DADOS_GAIN' 
     dirOffset   = dirMainData + '\\DADOS_OFFSET'
     
     # Checks if directories already exist, if negative, they are created, 
     # if positive, keep them
     x = os.listdir(diretory)
     for y in x:
          if y == 'DADOS':
               dirDADOS = 1
               x = os.listdir(dirMainData)
               for y in x:
                    if y == 'DADOS_GAIN':
                         DirGain = 1
                    if y == 'DADOS_OFFSET':
                         DirOffset = 1
     
     # Create directories
     if dirDADOS == 0:  os.makedirs(dirMainData)
     if DirGain == 0:   os.makedirs(dirGain)
     if DirOffset == 0: os.makedirs(dirOffset)

###############################################################################

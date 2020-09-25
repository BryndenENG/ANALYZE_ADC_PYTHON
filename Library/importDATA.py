###############################################################################
#IMPORT
import os
import pandas as pl
###############################################################################
def importDATA(dataAddress:str):
     'Function that enters the execution directory data, the csv files are read' 
     'in the DATA folder. The data is polished and the information of interest' 
     'is removed.'
     'Returns two lists, the first with the gain calibration values ​​and the' 
     'second with the offset calibration data with the list data in the data' 
     'format of the pandas library'
     
     dataAddress += '\\DADOS'

     #List all files and directories in the current directory
     addressFrame = os.listdir(dataAddress)
     
     # List all gain calibration files
     # List all offset calibration files
     listGain = []
     listOffset = []

     for x in addressFrame:
          if 'GAIN.csv' in x or 'OFFSET.csv' in x:
               a = dataAddress + '\\' + x
               if 'GAIN.csv' in x:
                    listGain.append(a)
               elif 'OFFSET.csv' in x:
                    listOffset.append(a)
     
     # Stores data, separating them into 2 databases
     dataGain = []
     dataOffset = []
     for x in listGain:
          dataGain.append(pl.read_csv(x))
     for y in listOffset:
          dataOffset.append(pl.read_csv(y))
     
     # Excluding columns that do not have relevant information
     dataGain = removeColumn(dataGain, 'Time [s]')
     dataGain = removeColumn(dataGain, 'Packet ID')
     dataOffset = removeColumn(dataOffset, 'Time [s]')
     dataOffset = removeColumn(dataOffset, 'Packet ID')

     #Delete line 0 to 14 for reading adc configuration message
     aux = 0
     for x in dataGain:
          for y in range(15):
               x = x.drop(y)
          dataGain[aux] = x
          aux += 1
     aux = 0
     for z in dataOffset:
          for t in range(15):
               z = z.drop(t)
          dataOffset[aux] = z
          aux += 1
     
     # Remove calibration command lines '0xF4'
     aux = 0
     for x in dataGain:
          filtro = x['MOSI'] != '0xF4'
          dataGain[aux] = x[filtro]
          aux +=1
     
     # Removes the calibration data from the table
     aux = 0
     for x in dataGain:
          filtro = x['MOSI'] == '0xFF'
          dataGain[aux] = x[filtro]
          aux +=1
     
     # MOSI column removal
     dataGain = removeColumn(dataGain, 'MOSI')

     # Remove offset command lines '0xF3'
     aux = 0
     for x in dataOffset:
          filtro = x['MOSI'] != '0xF3'
          dataOffset[aux] = x[filtro]
          aux +=1
     
     # Removes the calibration data from the table
     aux = 0
     for x in dataOffset:
          filtro = x['MOSI'] == '0xFF'
          dataOffset[aux] = x[filtro]
          aux +=1
     
     # MOSI column removal
     dataOffset = removeColumn(dataOffset, 'MOSI')
     
     return dataGain, dataOffset
###############################################################################
def removeColumn(dataFrame:list, column:str)->list:
     'Dataframe column removal'
     aux = 0
     for x in dataFrame:
          del x[column]
          dataFrame[aux] = x
          aux += 1
     return dataFrame
###############################################################################
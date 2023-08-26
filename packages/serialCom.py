
from abc import abstractmethod
import serial 
from datetime import datetime


class SerialCom :
    
    def __init__(self) -> None:
        self.__ser = None
        self.__started = False
        
    @abstractmethod
    def findCom(baudrate=9600) -> list :
        """
        function : Des
        @param1 : 
        """
        
        listAvailableComs = []
        for i in range(20) :
            COM = '/dev/ttyACM'
            try :
                ser = serial.Serial(port=COM + str(i), baudrate=baudrate)
                listAvailableComs.append(COM+str(i))
            except :
                #pass
                #print("no card found")
                break
        return listAvailableComs

    def startCom(self, port, baudrate=9600):
        self.__ser = serial.Serial(port=port, baudrate=baudrate)
        self.__started = True

    #def readLine(self):
     #   if self.__started :
      #      serialBytes = self.__ser.readline()
       #     return serialBytes.decode().rstrip()
        
        
        
        
        #else :
         #   raise Exception("Error reading serial")
    def readLine(self):
        data ={}
        values = []
        sensors = []
        if self.__started :
            serialBytes = self.__ser.readline()
            
            bruteData = serialBytes.decode().rstrip()
            
                #Sensors.append(value) print(values)
                
            return serialBytes.decode().rstrip()
        
        
        
        
        else :
            raise Exception("Error reading serial")
    
def closeCom(self):
        if self.__started :
            self.__ser.close()
        else :
            raise Exception("Error closing serial")

    # def __del__(self):
    #     self.closeCom()


if __name__ == "__main__" :
    print(SerialCom.findCom())

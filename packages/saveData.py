import serial
from datetime import datetime
import pandas

ser = serial.Serial(port='COM3', baudrate=9600)
data= {}
 

def main(): 
    time = []
    values = []
    sensors = []
    while True :
        serialBytes = ser.readline()
        bruteData = serialBytes.decode().rstrip()
        print(bruteData)
        sensor , value = bruteData.split(":")
        print("Recieved data in {} from {} {}".format(datetime.now(),sensor, value))
        if sensor in data.keys():
            values = data[sensor]["values"]
            values.append(value)
            times = data[sensor]["time"]
            times.append(datetime.now())
            data[sensor]["values"] = values
            data[sensor]["time"] = times
           
        else :
               data[sensor] = {
            "values" : [value],
            "time" : [datetime.now()]
            }
        
if __name__=='__main__': 
    try: 
        main()
    except KeyboardInterrupt :
        
        for sensor in data :
            print(data[sensor])
            pd =pandas.DataFrame(data[sensor])
            print(pd.head())
            pd.to_csv(sensor + ".csv", index=False)
    #data =pandas.DataFrame({"time" : time, "sensor": sensors, "value": values})
    #print(data.head())
    #data.to_csv("sensori.csv")
    
         
    
    



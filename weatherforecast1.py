import forecastio
import pylab as pyl
import numpy as np

api_key = "fd836b581d833e547d33c1a609f923af"
lat = np.zeros(4)
lng = np.zeros(4)

lat[0] = 32.7355556    #Arlington, TX
lng[0] = -97.1077778


lat[1] = 37.773972    #San Fransico, CA
lng[1] = -122.431297


lat[2] = 41.6005556   #Des Moines, IA
lng[2] = -93.6088889


lat[3] = 40.748817    #NYC, NY
lng[3] = -73.985428


forecast = [None]*4
byHour = [None]*4
T = np.zeros((4, 49))


for  i in range(0,4):
    forecast[i] = forecastio.load_forecast(api_key, lat[i], lng[i])
    byHour[i] = forecast[i].hourly()
    print byHour[i].summary
    print byHour[i].icon
    n=0
    for hourlyData in byHour[i].data:
        T[i,n]=hourlyData.temperature
        n=n+1

    


pyl.plot(T[0,:],'r--', label='Arlington', linewidth=3)
pyl.plot(T[1,:],'b--',label='San Fransico',linewidth=3)
pyl.plot(T[2,:],'k--',label='Des Moines',linewidth=3)
pyl.plot(T[3,:],'g--',label='NYC',linewidth=3)
pyl.legend()
pyl.xlabel('Hour')
pyl.ylabel('Temprature, F')
pyl.title('Last 50 Hours Temprature')
pyl.grid(True)
pyl.show()

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = Dataset(r'E:\internship\netCDF4\rtofs_glo_3dz_f006_6hrly_reg3.nc')

lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
tave = data.variables['tave'][:]

mp = Basemap(projection = 'merc',
             llcrnrlon = 42.8,
             llcrnrlat = -2,
             urcrnrlon = 105.37,
             urcrnrlat = 38.78,
             resolution = 'i')

lon, lat = np.meshgrid(lons, lats)
x,y = mp(lon, lat)

c_scheme = mp.pcolor(x, y, np.squeeze(tave[0,:,:]), cmap = 'jet')
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()

cbar = mp.colorbar(c_scheme, location = 'right', pad = '19%')

plt.title('Average Temparature on 01-01-1962')
plt.show()












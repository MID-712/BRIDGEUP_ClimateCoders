#Import packages
#in order to run code
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

#navigates to our data folder	
	dataPath = '/Users/brownscholar/Dropbox/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2009.nc')
#opens the file
#set variables	
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]
	
#get all of the values for each variable via slicing	
	condition_depth = depth <= 20
#Corals don't grow past 20 meters
	temp_sliced = temp[:,condition_depth,:,:]
	# print (temp_sliced.shape)
	#print (temp.shape)
	lat_condition = (lat >= -10) & (lat <= 10)
	lat_sliced = lat[lat_condition]
	print(lat_sliced.shape)

	lon_condition = (lon >= 100) & (lon <= 150)
	lon_sliced = lon[lon_condition]
	print(lon_sliced.shape)

#creates average temperature	
	temp_mean = temp_sliced.mean()
	#print (temp_mean)

	# print (lon.shape)
	# print (lat.shape)

	temp_conditioned1 = temp[:,condition_depth,:,:]

	temp_conditioned2 = temp_conditioned1[:,:,lat_condition,:]

	temp_conditioned3 = temp_conditioned2[:,:,:,lon_condition]

	temp_anom = temp_conditioned3 - temp_mean

	#temp_anom = temp[:,condition_depth,:,:] - temp_mean
	#print (temp_anom.shape)
	temp_anom_year = temp_anom.mean(axis = 0).shape
	temp_anom_depth =  temp_anom.mean(axis = 1).shape
	temp_anom_lon = temp_anom.mean(axis = 2).shape
	temp_anom_lat = temp_anom.mean(axis = 3).shape

	temp_anom_year_depth = temp_anom.mean(axis = 0).mean(axis = 0)	
	#print (temp_anom.mean(axis = 0).mean(axis = 0).shape)
	#print (temp_anom_year_depth)

	#print(temp_mean)
	#print(temp_sliced.shape)
	
	# plt.figure()
	# ax_f = plt.contourf(lon,lat,temp_anom_year_depth)
	# ax = plt.contour(lon,lat,temp_anom_year_depth, colors = 'black')
	# plt.pcolor(lon, lat, temp_anom_year_depth[:,:], cmap="plasma")
	# plt.title(("2009 Sea Surface Temperature Anomaly"), color= "darkmagenta")
	# plt.xlabel("Longitude", color='darkmagenta')
	# plt.ylabel("Latitude", color='darkmagenta')
	# plt.show()

	plt.figure()
	ax_f = plt.contourf(lon_condition,lat_condition,temp_anom_year_depth)
	ax = plt.contour(lon_condition,lat_condition,temp_anom_year_depth, colors = 'black')
	plt.pcolor(lon_condition, lat_condition, temp_anom_year_depth[:,:], cmap="plasma")
	plt.title(("2009 Sea Surface Temperature Anomaly"), color= "darkmagenta")
	plt.xlabel("Longitude", color='darkmagenta')
	plt.ylabel("Latitude", color='darkmagenta')
	plt.show()

#Execute main script
if __name__ == '__main__':
	main()

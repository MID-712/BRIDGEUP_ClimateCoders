#Import packages
import os
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sst_anomaly_functions

#Create functions

#Main script
def main():

	
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	os.chdir(dataPath)
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2015.nc')

	
	lon = data.variables['xt_ocean'][:]
	lat = data.variables['yt_ocean'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean'][:]
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	
	condition_depth = depth <= 20
	temp_sliced = temp[:,condition_depth,:,:]

	
	temp_mean = temp_sliced.mean()
	
	
	temp_anom = temp[:,condition_depth,:,:] - temp_mean

#Execute main script
if __name__ == '__main__':
	main()

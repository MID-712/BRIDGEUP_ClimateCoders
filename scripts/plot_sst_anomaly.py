#Import packages

#Create functions

#Main script
def main():

	#Step 1: Import data file
	dataPath = '/Users/hellenfellow/Dropbox (AMNH)/BridgeUP_ClimateCoders/Data'
	data = Dataset('compressed_soda3.12.2_mn_ocean_reg_2017.nc')

	#Step 2: Save the necessary variables
	lon = data.variables['lon'][:]
	lat = data.variables['lat'][:]
	time = data.variables['time'][:]
	depth = data.variables['st_ocean']
	temp = data.variables['temp'][:]
	salt = data.variables['salt'][:]

	#Step 3: Find mean SST
	temp_mean = temp[:,:,:,:].mean()

	#Step 4: Find SST anomaly
	temp_anom = temp - temp_mean

#Execute main script
if __name__ == '__main__':
	main()
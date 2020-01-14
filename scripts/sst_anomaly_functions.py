import os
from netCDF4 import Dataset
import numpy as np

def find_long_term_average_temperature(data_path,maxDepth):
	'''
	Finds long-term average of sea temperature. 

	Inputs:
	maxDepth = maximum depth to average over
	data_path = path to folder where data is stored

	Outputs:
	mean_temp = long-term average of temperature

	'''

	#Change directory
	os.chdir(data_path)

	#Save file names into list
	file_dir = os.listdir()
	file_dir = [i for i in file_dir if 'compressed_' in i]

	#Calculate average temperature and salinity
	mean_temp = []
	for i,file in enumerate(file_dir):
		data_file = Dataset(file)
		depth_file = data_file.variables['st_ocean'][:]
		boolDepth = depth_file <= maxDepth
		temp_file = data_file.variables['temp'][:]
		temp_file = temp_file[:,boolDepth,:,:].mean(axis = 1)
		mean_temp.append(temp_file)
	mean_temp = np.array(mean_temp)
	mean_temp = mean_temp.mean(axis = 0)
	mean_temp = np.ma.masked_values(mean_temp, mean_temp.min())

	return mean_temp

def find_long_term_average_salinity(data_path,maxDepth):

	'''
	Finds long-term average of sea salinity. 

	Inputs:
	maxDepth = maximum depth to average over
	data_path = path to folder where data is stored

	Outputs:
	mean_temp = long-term average of salinity 

	'''

	#Change directory
	os.chdir(data_path)

	#Save file names into list
	file_dir = os.listdir()
	file_dir = [i for i in file_dir if 'compressed_' in i]

	#Calculate average temperature and salinity
	mean_salt = []
	for i,file in enumerate(file_dir):
		data_file = Dataset(file)
		depth_file = data_file.variables['st_ocean'][:]
		boolDepth = depth_file <= maxDepth
		salt_file = data_file.variables['salt'][:]
		salt_file = salt_file[:,boolDepth,:,:].mean(axis = 1)
		mean_salt.append(salt_file)
	mean_salt = np.array(mean_salt)
	mean_salt = mean_salt.mean(axis = 0)
	mean_salt = np.ma.masked_values(mean_salt, mean_salt.min())

	return mean_salt




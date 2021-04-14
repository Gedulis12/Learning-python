import requests
import pandas as pd
import json


response = requests.get('https://prices.runescape.wiki/api/v1/osrs/latest') #Get price data

iteminfo = requests.get('https://prices.runescape.wiki/api/v1/osrs/mapping') #Get items data

items_data = iteminfo.json() #convert item data to readable JSON file

raw_data = response.json() #convert price data to readable JSON file
response_data = raw_data['data'] #Strip JSON file of 'parent' key (required to be able t work with data)


#####################################################
#ATTMPTED THIS:
#for key in response_data:
	#print(key, ":", response_data[key])
#	df = pd.DataFrame()
#	id_list = [key]
#	high_price_list = response_data[key]['high']
#	df['IDs'] = id_list
#	df['high_price'] = high_price_list
#####################################################

# Data frame with price data:
df1 = pd.DataFrame(response_data) #Put price data to dataframe
df1 = df1.transpose() #Transpose dataframe
df1 = df1.reset_index() #Remove index (make it as a column)
#df1 = df1.set_index('index') - sets ID as index
df1['high-low'] = df1['high'] - df1['low'] #Add pricediff column
df1['Profit margin'] = (df1['high'] / df1['low']) - 1
df1.rename(columns = {'index': 'id'}, inplace = True) #Rename ID column
df1['id'] = df1['id'].astype(int) #Change ID datatype to INT

#df1.to_csv (r'~/Projects/Own projects/test.csv') - exports CSV file
#print(df1)


#Data frame with info about items (used to ookup item names):
df2 = pd.DataFrame.from_records(items_data) #put items data to dataframe
df2['id'] = df2['id'].astype(int) #Change ID datatype to INT
#df2.to_csv (r'~/Projects/Own projects/df2.csv') - exports CSV fille


#Data frame with price data and item names:
df3 = pd.merge(df1, df2[['name','id']], on = 'id', how = 'left') #Adds item name as a column
df3 = pd.merge(df3, df2[['limit','id']], on = 'id', how = 'left') #Adds trading limit
#df3.to_csv (r'~/Projects/Own projects/df3.csv') - exports CSV fille
print(df3)
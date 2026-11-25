# importing the requests library
import requests
import json
import csv

# api-endpoint
# URL = "http://maps.googleapis.com/maps/api/geocode/json"
URL = "http://api.exchangeratesapi.io/v1/symbols?access_key=e72e8e07df45a5ac9e794caf4a409f21"
# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(URL)
print(r.status_code)

# extracting data in json format
data = r.json()
print(data)
symbol_data = data["symbols"]

with open('symbols.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))


# # now we will open a file for writing
# data_file = open('symbols.csv', 'w')

# # create the csv writer object
# csv_writer = csv.writer(data_file)

# # Counter variable used for writing
# # headers to the CSV file
# count = 0

# for symbol in symbol_data:
# 	# if count == 0:

# 	# 	# Writing headers of CSV file
# 	# 	header = movie.keys()
# 	# 	csv_writer.writerow(header)
# 	# 	count += 1

# 	# Writing data of CSV file
# 	print(symbol)
# 	csv_writer.writerow(symbol)

# data_file.close()

#!/usr/bin/env python

import sys
import os
import glob
import csv

	
def main():
	parseFiles('US', 'New York', 'Erie')
	return

def parseFiles(whatCountry, whatState, whatCounty):
	dayData = {}
	for file in sorted(glob.glob('*.csv')):
		confirmed = 0
		deaths = 0
		recovered = 0
		active = 0
		with open(file, newline='') as csvfile:
		
			reader = csv.DictReader(csvfile)
			for row in reader:	

				# fix these two up since the files have different column names
				if 'Country_Region' in row:
					country = row['Country_Region']
				elif 'Country/Region' in row:
					country = row['Country/Region']
				else:
					country = ''

				if 'Province_State' in row:
					state = row['Province_State']
				elif 'Province/State' in row:
					state = row['Province/State']
				else:
					state= ''


				if country == 'US':
					if state == 'New York':
						confirmed += int(row['Confirmed'])
						deaths += int(row['Deaths'])
						recovered += int(row['Recovered'])
						if 'Active' in row:
							active += int(row['Active'])
#					print(row)

			dayData[os.path.splitext(file)[0]] = {'Confirmed':confirmed, 'Deaths':deaths, 'Recovered':recovered, 'Active':active}


	confirmed = []
	deaths = []
	for k,v in dayData.items():
		print (k,v)
		confirmed.append(int(v['Confirmed']))
		deaths.append(int(v['Deaths']))

	print(confirmed)
	print(deaths)
	
if __name__=="__main__":
	main()

	

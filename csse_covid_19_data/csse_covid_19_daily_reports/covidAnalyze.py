#!/usr/bin/env python

import sys
import os
import glob
import csv
import argparse

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


	
def main(Country, State, County):
	parseFiles(Country, State, County)
	return

def parseFiles(whatCountry, whatState, whatCounty):
	dayData = {}
	for file in sorted(glob.glob('*.csv')):
		confirmed = 0
		deaths = 0
		recovered = 0
		active = 0
		date = file


#		doCountry = not 
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

				if 'Admin2' in row:
					county = row['Admin2']
				else:
					county = None

				# pick the rows of interest
				if not whatCountry or country == whatCountry:
					if not whatState or state == whatState:
						if not whatCounty or county == whatCounty:
							# some records have '' rather than 0
							if row['Confirmed']:
								confirmed += int(row['Confirmed'])

							if row['Deaths']:
								deaths += int(row['Deaths'])

							if row['Recovered']:
								recovered += int(row['Recovered'])

							if 'Active' in row:
								active += int(row['Active'])

			# put the totals together and use the date string as the key
			dayData[os.path.splitext(file)[0]] = {'Confirmed':confirmed, 'Deaths':deaths, 'Recovered':recovered, 'Active':active}
	




	confirmed = []
	deaths = []
	# grab thins in lists since they are easier to work with
	for k,v in dayData.items():
		confirmed.append({'Date':k, 'Confirmed':int(v['Confirmed'])})

		deaths.append({'Date':k, 'Deaths':int(v['Deaths'])})


	# get the stats for each day
	dk = [i['Date'] for i in confirmed[1:]]
	dv = np.diff([i['Confirmed'] for i in confirmed])
	dailyConfirmed = list(zip(dk, dv))

	dk = [i['Date'] for i in deaths[1:]]
	dv = np.diff([i['Deaths'] for i in deaths])
	dailyDeaths = list(zip(dk, dv))

	c = [i['Confirmed'] for i in confirmed]
	d = [i['Deaths'] for i in deaths]
	plt.subplot(2,1,1)
	plt.plot(c)
	plt.subplot(2,1,2)
	plt.plot(d)
	plt.show()

'''
	# print everything out 
	print('\n'.join(['{} : {}'.format(i['Date'], i['Confirmed']) for i in confirmed]))
	print('\n')
	print('\n'.join(['{} : {}'.format(i[0], i[1]) for i in dailyConfirmed]))
	print('\n')

	print('\n'.join(['{} : {}'.format(i['Date'], i['Deaths']) for i in deaths]))
	print('\n')
	print('\n'.join(['{} : {}'.format(i[0], i[1]) for i in dailyDeaths]))
	print('\n')

	print('\n')

	# So 543 US solders died in combar during the Tet Offensive in
	# ONE WEEK in Feb 1968, we are comparing this to NYC COVID deaths per DAY
	TetDeaths = 543
	print('\n'.join(['{} : {}'.format(i[0], i[1]) for i in dailyDeaths if i[1] > TetDeaths]))
'''


	


if __name__=="__main__":
   
	namesp = __import__(__name__)
	parser = argparse.ArgumentParser()
	parser.add_argument("-C", help="Collect record for country", action='store')
	parser.add_argument("-s", help="collect records for state", action='store')
	parser.add_argument("-c", help="collect records for county", action='store')
	args = parser.parse_args()

	main(args.C, args.s, args.c)

	

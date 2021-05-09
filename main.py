from datetime import datetime
from calendar import monthrange
from datetime import date
from datetime import timedelta

import config
import requests
from requests_html import HTMLSession
import pickle

import urllib

import os.path
from urllib.request import urlopen


def parse_date(date):
	return date.year, date.month, date.day


def get_remaining_days(date):
	_, remaining_days = monthrange(date.year, date.month)
	return remaining_days


def convert_to_24_hour_time(time):
	time = datetime.strptime(time, "%I:%M %p")
	return datetime.strftime(time, "%H:%M")


def modify(time):
	time = time[0].strip()
	return convert_to_24_hour_time(time)


def get(date):
	url = f"https://www.timeanddate.com/sun/@{config.LATITUDE},{config.LONGITUDE}"
	session = HTMLSession()
	response = session.get(url)

	_, _, day = parse_date(date)

	xpath_sunrise = f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[1]/text()'
	xpath_sunset = f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[2]/text()'

	sunrise =  response.html.xpath(xpath_sunrise)
	sunset =  response.html.xpath(xpath_sunset)

	sunrise = modify(sunrise)
	sunset = modify(sunset)
	return sunrise, sunset


def get_all(date):
	arr = []
	for day in range(date.day, get_remaining_days(date)+1):
		next_date = date + timedelta(day - date.day)

		sunrise, sunset = get(next_date)
		next_data = f"{sunrise} - {sunset}"

		tmp = {"date": next_date, "data": next_data, 'coordinates': (config.LATITUDE, config.LONGITUDE)}
		arr.append(tmp)
		save_data(arr)

	return arr

def save_data(arr):
	with open(config.DATA_PATH, "wb") as file:
		pickle.dump(arr, file)


def load_data():
	with open(config.DATA_PATH, "rb") as file:
		arr = pickle.load(file)
	return arr


def connected():
	try:
		response = urlopen('https://www.google.com/', timeout=10)
		return True
	except:
		return False


def file_exist():
	return os.path.isfile(config.DATA_PATH)


def main():
	today = date.today()

	if file_exist():
		arr = load_data()
		if today == arr[0]['date'] and arr[0]['coordinates'] == (config.LATITUDE, config.LONGITUDE):
			data = arr[0]['data']
			print(data)

	else:
		if not connected():
			print("offline and no data available")
		else:
			arr = get_all(today)
			data = arr[0]['data']
			print(data)


if __name__ == '__main__':
	main()
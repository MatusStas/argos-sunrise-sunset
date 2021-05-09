from datetime import datetime
from requests_html import HTMLSession
import requests
import config
import sys


def get_day_of_month():
	day = datetime.now()
	return int(day.strftime("%d"))


def convert_to_24_hour_time(time):
	time = datetime.strptime(time, "%I:%M %p")
	return datetime.strftime(time, "%H:%M")


def modify(time):
	time = time[0].strip()
	return convert_to_24_hour_time(time)


def get_data():
	url = f"https://www.timeanddate.com/sun/@{config.LATITUDE},{config.LONGITUDE}"
	session = HTMLSession()
	response = session.get(url)

	day = get_day_of_month()

	xpath_sunrise = f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[1]/text()'
	xpath_sunset = f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[2]/text()'

	sunrise =  response.html.xpath(xpath_sunrise)
	sunset =  response.html.xpath(xpath_sunset)

	sunrise = modify(sunrise)
	sunset = modify(sunset)
	return sunrise, sunset


def main():
	sunrise, sunset = get_data()
	out = f"{sunrise} - {sunset}"
	print(out)


if __name__ == '__main__':
	main()
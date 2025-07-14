# Import pandas as pd
import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

# The url to find the red wine quality data set is
# https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

# Using urlretrieve to save the file locally as winequality-red.csv
urlretrieve(url,filename='winequality-red.csv')

#Checking data fetched
df = pd.read_csv('winequality-red.csv', sep=";")
print(df.head())

# Print the column names
print(df.columns)

# Assign the 'alcohol' column of the DataFrame to the variable alcohol.
alcohol = df['alcohol']
print(alcohol)

# We can pull and save Excel files
url = "https://www2.census.gov/programs-surveys/cbp/datasets/2022/cbp22cd.xlsx"

# Read in all sheets of Excel file: xlsx
xlsx = pd.read_excel(url, sheet_name=None)

# Using .keys(), print the sheetnames to the shell
print(xlsx.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xlsx['cbp22cd'].head())



# Performing HTTP requests in Python using urllib
# Import urlopen and Request from the urllib.request packages
from urllib.request import urlopen, Request
url = "https://www.nysed.gov/news/2024/2019-cohort-graduation-data"

# Using Requests(), packages the request: request
request = Request(url)

# Urlopen sends the request and catches the response.
response = urlopen(request)

# Print the datatype of response
print(type(response))

response.close()


# Import packages
from urllib.request import urlopen, Request

# Scrapping wikipedia.org
url = "https://www.wikipedia.org"

request = Request(url)

response = urlopen(request)

html = response.read()

# Print the html
print(html)

response.close()


# Import package requests
import requests

# Specify the url: url
url = "https://www.buffalo.edu/"

r = requests.get(url)

text = r.text

# Print the html
print(text)


# Using BeautifulSoup
from bs4 import BeautifulSoup

# We'll pull data from the url 'https://www.python.org/~guido/'
# Specify url: url
url= "https://www.python.org/~guido/"

# Package the request, send the request, and catch the response: r
r = requests.get(url)

# extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object using .prettify() method of soup.
pretty_soup= soup.prettify()

# Print the response
print(pretty_soup)

# Using .title, get the title of Guido's webpage from soup.
guide_title= soup.title
print(guide_title)

guido_text = guide_title.get_text()

# Print Guido's text to the shell
print(guido_text)


# Using .find_all(), find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Using a for loop, print the URLs to the shell
for link in a_tags:
    print(link.get('href'))



# Pulling JSON data
# Assign URL to variable: url
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

r = requests.get(url)

# Using .json(), decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print json_data
print(json_data)

# Print the Wikipedia page extract
print(json_data['query']['pages']['24768']['extract'])




# API and Authentication
# Via https://openweathermap.org/appid

# First, set your API key to a variable: api_key
api_key = "5cb7d7868090d9b24bc05d27a3f7b6e3"
lat = 42.88
lon = -78.88
url = 'https://api.openweathermap.org/data/2.5/forecast?lat='+str(lat)+'&lon='+str(lon)+'&appid='+api_key
print(url)

response = requests.get(url)

# Response
print(type(response))

# Decoding the JSON data into a dictionary: response_json
response_json = response.json()

print(response_json)

# Using a for loop to print the
# key and value pairing of the JSON
for key, value in response_json.items():
    print(key)
    print(value)

# Print the values for the 'list' key.
temp_list = response_json['list']
print(temp_list)

# Print the type of this value
print(type(temp_list))


# Print the first element in the list.
print(temp_list[0])

# Print the values for the 'main' key in this first element in 'list'
print(temp_list[0]['main'])

# Make this a variable called temp
temp = temp_list[0]['main']['temp']

# Print the temperature in C
celsius_temp = temp - 273
print(celsius_temp)

# Assign the time element to a variable called time
time = temp_list[0]['dt_txt']
# Print time
print(time)
# Print the type
print(type(time))

# Import datetime from the datatime package.
import datetime
# Create a new variable with time converted to the datetime format.
# Using strptime() call this variable time_time.
time_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
# Print time_time
print(time_time)
# Print type of time_time
print(type(time_time))


# Using len(), print the length of 'list' in response_json
print(len(temp_list))

# Now let’s loop this JSON and pull out all of the temperatures and
# times.
temperatures = []
times = []
for data in temp_list:
    temperature = data['main']['temp'] - 273
    temperatures.append(temperature)
    times.append(data['dt_txt'])


print(temperatures)
print(times)



# Plotting graph
temperatures_pd = pd.DataFrame()
# Make the column temperature equal to the list temperatures
temperatures_pd['temperatures'] = temperatures
# Make the column time equal to the list time
temperatures_pd['time'] = times

print(temperatures_pd)

temperatures_pd.plot(kind='line')

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()

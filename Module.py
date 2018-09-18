from urllib import request
#import urllib.request
import random

def printSomething(value):
    print(value)

def download_url_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    request.urlretrieve(url, fullname)

def write_file(name):
    file = open('About ' + name + '.txt', 'w')
    file.write("He is good and intelligent\n")
    file.write("But he is very naughty too!")
    file.close()

def read_csvfile(samplecsv):
    response = request.urlopen(samplecsv)
    csv = response.read()
    csvData = str(csv).split('\\n')

    file = open("sample.csv", 'w')
    for csv in csvData:
        file.write(csv + '\n')
    file.close()
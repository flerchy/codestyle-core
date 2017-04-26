from urllib import request
#import urllib.request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=11&e=3&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def download(url):
    response = request.urlopen(url)
    csv=response.read()
    #process the file and store it in variable
    csv_str = str(csv)
    print(csv_str)
    #concver to string
    lines = csv_str.split("\\n")
    print(lines)
    #takes a long string and breaks it up
    des_url = r'goog.csv'
    # r mean raw, allowing you not to escape every character (dont need C:\\)
    fx = open (des_url, "w")
    for line in lines:
        fx.write(line + "\n")
        fx.close()

        download(goog_url)

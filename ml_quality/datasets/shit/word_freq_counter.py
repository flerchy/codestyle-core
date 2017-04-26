import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    list = []
    source = requests.get(url).text
    soup = BeautifulSoup(source)
    for list in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string
        #puts it into string
        words = content.lower().split()
        # puts all in lower case and splits ito keywords
        #stored in dictionary for no dupes
        for each_word in words
        list.append(each_word)
        clean_up_list(list)

def clean_up_list(list):
    clean_word_list = []
    for word in list
        ## regex symbols to remove
        symbols = "!@#$%^&*()[]_+?><{}:\""
        for i in range(0, len(symbols))
        word = world.replace(symbols[i],"")
        if len(word) > 0:
            clean_word_list.append(word)
            createdictionary(clean_word_list)

def createdictionary(clean_word_list):
    count={}
    for word in clean_word_list:
        if word in count
        count[word] += 1
    else:
        count[word] = 1
    #sorted goes through each item
    for key, value in sorted(count.items(),key=operator.itemgetter(1)):
        print(key,value)


start(url)

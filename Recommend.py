from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def main(emotion):
    if emotion=='Sad':
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Disgust':
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Anger':
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Anticipation':
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Fear':
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Enjoyment':
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Trust':
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif emotion=='Surprise':
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    
    response=HTTP.get(url)
    data=response.text
    
    soup=SOUP(data, 'lxml')
    
    title=soup.find_all('a', attrs={'href': re.compile(r'\/title\/tt+\d*\/')})
    return title

if __name__ == '__main__':
    emotion=input("How are you feeling today? \n")
    a=main(emotion)
    count=0

    if(emotion=='Disgust' or emotion=='Anger' or emotion=='Surprise'):
        for i in a:
            tmp=str(i).split('>;')
            if len(tmp)==3:
                print(tmp[1][:-3])
            if count>13:
                break
            count+=1
    else:
        for i in a:
            tmp=str(i).split('>')
            if len(tmp)==3:
                print(tmp[1][:-3])
            if count>11:
                break
            count+=1
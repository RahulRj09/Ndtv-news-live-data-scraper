import requests
from bs4 import BeautifulSoup as bs
source = requests.get("https://www.ndtv.com/latest?pfrom=home-topnavigation").text
soup = bs(source,'html5lib')
url= []
soup = soup.find('div',{'class': 'new_storylising'})
for i in soup.find_all("a"):
	 try:
	 	if (i['href'].startswith('/') or "ndtv" in i['href']):
	 		if i['href'] not in url:
	 			url.append(i["href"])
	 		else:
	 			continue
	 except KeyError:
           pass	

total_news = 1;
for i in range(len(url)):
	try:
		r = requests.get(url[i])
		title = bs(r.content, 'html5lib') 
		print(total_news,"Title = ",title.title.string)
		news_div = title.find('div', {'class': 'ins_dateline'})
		author = news_div.find('span', {'itemprop': 'name'})
		print("Author = ",author.string)
		date = title.find('span', {'itemprop': 'dateModified'})
		print("Date = ",date.string)
		article_div = title.find('div', {'id': 'ins_storybody'})
		article_p = article_div.findAll('p')
		print("Article = ")
		for i in article_p:
			try:
				if "None" in i.string:
					continue
				else:	
					print(i.string)
			except TypeError:
				pass
		total_news +=1
		print("--!--=--!--=--!--=--!--=--!--=--!--=--!--=----!!!!!----=--!--=--!--=--!--=--!--=--!--=--!--=--!--")
	except AttributeError:
		pass
		

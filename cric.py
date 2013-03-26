from flask import Flask
from BeautifulSoup import BeautifulSoup
from requests import get

app = Flask (__name__)

@app.route('/')
def index():
	body = """<META HTTP-EQUIV="REFRESH" CONTENT="2">"""
	body = body + get_score (get_page ())
	return body

def get_score (page):
	data = BeautifulSoup (page)
	elements = data.findAll ('div', {'class':'headLeftDiv'})
#	table = elements = data.findAll ('div', {'class':'mainScoreTable'})
#	body = str(elements) + str (table)
	return str (elements)
	
def get_page ():
	return get ('http://www.espncricinfo.com/netstorage/598815.html').text

if __name__ == "__main__":
	app.run (host='0.0.0.0')

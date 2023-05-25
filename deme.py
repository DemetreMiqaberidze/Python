import requests
import json
import sqlite3
from win10toast import ToastNotifier
url = "https://anime-db.p.rapidapi.com/anime"
title=input('say name')
querystring = {"page":"1","size":"10","search":title}

headers = {
	"X-RapidAPI-Key": "bb69010caemsh9845993d1ae2a36p1fcbacjsn64da58e9e82f",
	"X-RapidAPI-Host": "anime-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#1.
# print(response.status_code())
# print(response.headers)
# print(response.text)
#2.
# with open( 'text.json', 'w' ) as file:
#     json.dump( response.json(), file, indent=4 )

#3.
# conn = sqlite3.connect('iloveanime.sqlite')
# cur = conn.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS links
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title VARCHAR(50),
#         link VARCHAR(100))''')
# cur.execute( "INSERT INTO links (title,link) VALUES (?, ?)", (title, response.json()['data'][0]['link']) )
# conn.commit()
# cur.close()
# conn.close()

#4.

#5.
# notification = ToastNotifier()
# notification.show_toast( title, "founded successful",duration=5 )
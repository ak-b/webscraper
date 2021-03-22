from bs4 import BeautifulSoup

page = requests.get("https://<URL OF INTEREST")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>

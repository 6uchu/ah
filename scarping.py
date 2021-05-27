from requests_html import HTMLSession

session = HTMLSession()

url = 'https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko'

r = session.get(url)

r.html.render(sleep=1, scrolldown = 5)

articles = r.html.find('article')
newslist = []

for item in articles:
    try:
        newsitem = item.find('h3', first = True)
        newsarticle = {
        'title' : newsitem.text,
        'link' : newsitem.absolute_links
        }
        newslist.append(newsarticle)
        # title = newsitem.text
        # link = newsitem.absolute_links
        # print(title, link)
    except:
        pass

for i in newslist:
    print(i)
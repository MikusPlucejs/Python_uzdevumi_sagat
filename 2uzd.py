""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

"""
import feedparser
rss_url='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

lll=feedparser.parse(rss_url)

for entry in lll.entries:
    print('Virsraksts:', entry.title)
    print('Saite:', entry.link)
    print('Datums:', entry.published)
    print('\n')
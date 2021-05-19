from database import LinksDb
from googlesearch import search, get_random_user_agent
from time import sleep


class SearchWorker(object):
    """scrapping worker"""
    def __init__(self, mysearch):
        self.mysearch = mysearch
        self.links = LinksDb().getLinksStr(LinksDb().getLinks())

    def worker(self, pipe):
        for url in search(self.mysearch, user_agent=get_random_user_agent(), pause=5):
            if not url in self.links:
                pipe.send(f"{self.mysearch} {url}")
                LinksDb().addLink(link=url, keyword=self.mysearch)
                self.links.append(url)
                sleep(2)

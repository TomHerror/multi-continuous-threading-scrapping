from singleton_decorator import singleton
from pony.orm import select, db_session
from .db import Db
from models import Link


@singleton
class LinksDb():
    """Class who communicate with link table in DB"""
    def __init__(self):
        self.database = Db().getDb()
        self.database.generate_mapping(create_tables=True)

    @db_session
    def getLinks(self) -> [Link]:
        return list(select(l for l in Link))

    def getLinksStr(self, links: [Link]) -> [str]:
        return [Link.link for link in links]

    @db_session
    def addLink(self, link: str, keyword: str) -> None:
        link = Link(link=link, keyword=keyword)
        return

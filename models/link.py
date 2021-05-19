from pony.orm import PrimaryKey, Required
from database import Db


class Link(Db().database.Entity):
    id: int = PrimaryKey(int, auto=True)
    link: str = Required(str)
    keyword = Required(str)


from sql_func import *


class People:
    def __init__(self, *args) -> None:
        self.userid: str = args[0]
        self.fname: str = args[1]
        self.money: int = args[2]

    def save_people(self, db):
        for t in ["userid", "fname", "money"]:
            db.update("userid", self.userid, t, eval(f"self.{t}"))

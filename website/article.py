import os
import datetime


    




class article():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = "2020-01-01"

    
    def get_date(self):
        d,m,y = self.date.split("-")
        return datetime.date(int(y),int(m),int(d))
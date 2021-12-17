from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
from . import api
import os
import pandas as pd

GENRES = api.MOVIEDB_API_GENRES()

def filterResults(object):
    genres = object['genre_ids']
    
    genres = [item['name'] for item in GENRES if item['id'] in genres]
    genres = ";".join(genres)

    return {
        'title': object['title'],
        'overview': object['overview'],
        "popularity": object['popularity'],
        'release_date': object['release_date'],
        'genres': genres
    }

class Bot(DesktopBot):
    def action(self, execution=None):
        response = api.MOVIEDB_API_ENDPOINT()
        data = list(map(filterResults, response))
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(os.path.dirname( __file__ ), 'botCityData.csv'), index=False)

        self.browse("https://docs.google.com/spreadsheets/u/0/")
        
        
        if not self.find( "blank", matching=0.97, waiting_time=10000):
            self.not_found("blank")
        self.click()
        
        
        self.wait(4000)
        if not self.find( "logo", matching=0.97, waiting_time=10000):
            self.not_found("logo")
        self.click_relative(64, 7)
        self.paste("BotCity spreadsheet")
        self.enter()

        # self.wait(4000)
        if not self.find( "file", matching=0.97, waiting_time=10000):
            self.not_found("file")
        self.click()

        if not self.find( "import", matching=0.97, waiting_time=10000):
            self.not_found("import")
        self.click()
        
        if not self.find( "upload", matching=0.97, waiting_time=10000):
            self.not_found("upload")
        self.click()
        
        if not self.find( "select", matching=0.97, waiting_time=10000):
            self.not_found("select")
        self.click()
        
        if not self.find( "arrowUp", matching=0.97, waiting_time=10000):
            self.not_found("arrowUp")
        self.click_relative(260, 6)
        
        dataPath = os.path.abspath(os.path.dirname( __file__ ))
        self.paste(dataPath)
        self.enter()
        
        if not self.find_text( "botcitydatacsv", threshold=230, waiting_time=10000):
            self.not_found("botcitydatacsv")
        self.double_click()
        
        if not self.find( "importdata", matching=0.97, waiting_time=10000):
            self.not_found("importdata")
        self.click()
        
        if not self.find( "opendata", matching=0.97, waiting_time=10000):
            self.not_found("opendata")
        self.click()
        self.wait(3000)
        
        # OLD IDEA
        # length = len(data)
        # # for i in range(length):
        # for i in range(7):
        #     if i == 0:
        #         for key in data[i].keys():
        #             self.paste(key)
        #             self.type_right()
        #     else:
        #         for value in data[i].values():
        #             self.paste(value)
        #             self.type_right()
        #     self.enter()
        #     self.enter()
        #     for _ in range(len(data[i].keys())):
        #         self.type_left()
        # self.control_a()
        # self.control_a()
        # if not self.find("fx", matching=0.97, waiting_time=10000):
        #     self.not_found("fx")
        # self.double_click_relative(27, 29)
        # self.type_left()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()






























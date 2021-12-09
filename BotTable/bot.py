from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
from . import api

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

        self.browse("https://docs.google.com/spreadsheets/u/0/")
        
        if not self.find( "blank", matching=0.97, waiting_time=10000):
            self.not_found("blank")
        self.click_relative(70, -71)
        
        self.wait(4000)
        if not self.find( "title", matching=0.97, waiting_time=10000):
            self.not_found("title")
        self.click()
        self.paste("BotCity spreadsheet")
        self.enter()
        
        length = len(data)
        # for i in range(length):
        for i in range(6):
            if i == 0:
                for key in data[i].keys():
                    self.paste(key)
                    self.type_right()
            else:
                for value in data[i].values():
                    self.paste(value)
                    self.type_right()
            self.enter()
            self.enter()
            for _ in range(len(data[i].keys())):
                self.type_left()
        self.control_a()
        self.control_a()
        if not self.find( "fx", matching=0.97, waiting_time=10000):
            self.not_found("fx")
        self.double_click_relative(27, 29)
        self.type_left()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()













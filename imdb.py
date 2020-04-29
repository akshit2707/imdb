#!/usr/bin/python

import requests
import json

def imdb():

    print("\n[+] For better accuracy you can also provide release year")
    title = input("Enter the name of movie:- ")
    year = input("Enter release year (If don't know, type 'Enter'):- ")

    URL = "http://www.omdbapi.com/?apikey=5d584e39&t={}&y={}".format(title, year)

    page = requests.get(URL)
    data = page.json()
    rating = data['imdbRating']
    name = data['Title']
    actors = data['Actors']
    released = data['Released']
    genre = data['Genre']
    Director = data['Director']
    lang = data['Language']

    print()
    print("+----------------------------+")
    print(f"| [+]     Information   [+]  |")
    print("+----------------------------+")
    print(f"[*] Rating of {name} {year} is \"{rating}\"")
    print(f"[*] Actors:- {actors}")
    print(f"[*] Released date:- {released}")
    print(f"[*] Genre:- {genre}")
    print(f"[*] Director:- {Director}")
    print(f"[*] Language:- {lang}")


if __name__=='__main__':
    imdb()



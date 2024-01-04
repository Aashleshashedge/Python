import requests
import tkinter as tkinter

def getNews():
    api_key = "6a7bad81a7b741978e5d1bf603cb3afc"
    url = "https://newsapi.org/v2/top-headlines?country=ind&apikey="+api_key
    news = requests.get(url).jsoon()


    articles = news["articles"]
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news =my_articles[i] +"\n"

        print (my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")


button = tk.Button (canvas, font = 24, text = "Reload", command = getnews)
button.pack(pady = 20)

label = tk.label(canvas , font = 18, justify = "left")

label.pack(pady = 20)

getNews()

canvas.mainlop()
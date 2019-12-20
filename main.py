from twitterscraper.query import query_tweets
import tkinter as tk
import datetime as dt
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


def get_sentiment(tweet_text):
    sen = TextBlob(tweet_text)
    analysis = ''
    if sen.sentiment.polarity > 0:
        analysis = 'positive'
    elif sen.sentiment.polarity == 0:
        analysis = 'neutral'
    else:
        analysis = 'negative'
    return analysis


def scrape_tweets(query, start, end):
    # query = e1.get()
    # begin = dt.date(int(sYear.get()), int(sMonth.get()), int(sDay.get()))
    # end = dt.date(int(eYear.get()), int(eMonth.get()), int(eDay.get()))
    query = query
    begin = start
    end = end
    queried_tweets = query_tweets(
        query, 1000, begindate=begin, enddate=end, lang='english')
    #df = pd.DataFrame(t.__dict__ for t in queried_tweets)
    tweets = []
    for x in queried_tweets:
        cleaned_tweets = {}
        cleaned_tweets['text'] = x.text
        cleaned_tweets['sentiment'] = get_sentiment(x.text)
        tweets.append(cleaned_tweets)
    return tweets


def plotCircleGraph(tweets):
    total = 0
    pos = 0
    neg = 0
    neut = 0
    for i in tweets:
        total += 1
        if(i['sentiment'] == 'positive'):
            pos += 1
        elif(i['sentiment'] == 'negative'):
            neg += 1
        else:
            neut += 1
    labels = 'Negative', 'Positive', 'Neutral'
    sizes = [pos*1.0/total, neg*1.0/total, neut*1.0/total]
    colors = ['gold', 'lightcoral', 'yellowgreen', 'lightskyblue']
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


query = input('Enter a keyword :: ')
start_date = dt.date(2019, 11, 1)
end_date = dt.date.today()
tweets = scrape_tweets(query, start_date, end_date)
pos_tweets = []
neg_tweets = []
neut_tweets = []
for i in tweets:
    if(i['sentiment'] == 'positive'):
        pos_tweets.append(i)
    elif(i['sentiment'] == 'negative'):
        neg_tweets.append(i)
    else:
        neut_tweets.append(i)
 # ------------------Examples----------------------------
print("Positive Tweets Examples :: ")
if(len(pos_tweets) >= 10):
    for i in range(0, 10):
        print('- '+(pos_tweets[i])['text'])
else:
    for i in pos_tweets:
        print('- '+i['text'])
 # ------------------Examples----------------------------
print("Negative Tweets Examples :: ")
if(len(neg_tweets) >= 10):
    for i in range(0, 10):
        print('- '+(neg_tweets[i])['text'])
else:
    for i in neg_tweets:
        print('- '+i['text'])
 # ------------------Examples----------------------------
print("Neutral Tweets Examples :: ")
if(len(neut_tweets) >= 10):
    for i in range(0, 10):
        print('- '+(neut_tweets[i])['text'])
else:
    for i in neut_tweets:
        print('- '+i['text'])
# -----------------Pie Chart-----------------------------
plotCircleGraph(tweets)


# master = tk.Tk()
# labels
# tk.Label(master, text="Keyword").grid(row=0)
# tk.Label(master, text="Start Date").grid(row=1)
# tk.Label(master, text="End Date").grid(row=2)
# entry for query
# e1 = tk.Entry(master)
# entry for start date
# sYear = tk.Entry(master)
# sMonth = tk.Entry(master)
# sDay = tk.Entry(master)
# entry for end date
# eYear = tk.Entry(master)
# eMonth = tk.Entry(master)
# eDay = tk.Entry(master)
# placeholding values
# e1.insert(10, "keyword")
# sYear.insert(10, "YYYY")
# sMonth.insert(10, "MM")
# sDay.insert(10, "DD")
# eYear.insert(10, "YYYY")
# eMonth.insert(10, "MM")
# eDay.insert(10, "DD")

# e1.grid(row=0, column=1)
# sYear.grid(row=1, column=1)
# sMonth.grid(row=1, column=2)
# sDay.grid(row=1, column=3)

# eYear.grid(row=2, column=1)
# eMonth.grid(row=2, column=2)
# eDay.grid(row=2, column=3)

# tk.Button(master,
#          text='Quit',
#          command=master.quit).grid(row=4,
#                                    column=0,
#                                    sticky=tk.W,
#                                    pady=4)
# tk.Button(master, text='Run', command=scrape_tweets).grid(row=4,
#                                                               column=1,
#                                                               sticky=tk.W,
#                                                               pady=4)

# master.mainloop()

# tk.mainloop()

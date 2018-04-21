import praw, feedparser, os, time

#Initialisation
reddit = praw.Reddit(
    client_id=os.environ['ID'],
    client_secret=os.environ['SECRET'],
    password=os.environ['PASSWORD'],
    user_agent=os.environ['USERAGENT'],
    username=os.environ['USERNAME']
)

subreddit = reddit.subreddit(os.environ['SUBREDDIT'])
rss_url = os.environ['RSSURL']


if not os.path.isfile("postedarticles.txt"):
    postedArticles = []
else:
    with open("postedarticles.txt", "r") as f:
       postedArticles = f.read()
       postedArticles = postedArticles.split("\n")
       postedArticles = list(filter(None, postedArticles))

starttime=time.time()
interval = float(os.environ['INTERVAL'])
while True:
    feed = feedparser.parse(rss_url)
    print("Checking for new articles!")
    newArticles = 0
    for item in feed['items']:
        if item['id'] not in postedArticles:
            medial_url = item['media_content'][0]['url']
            subreddit.submit(item['title'], url=item['link'])
            postedArticles.append(item['id'])
            newArticles += 1
            time.sleep(30)
    print("{0} new articles found.".format(newArticles))

    with open("postedarticles.txt", "w") as f:
        for article_id in postedArticles:
            f.write(article_id + "\n")

    time.sleep(interval - ((time.time() - starttime) % interval))

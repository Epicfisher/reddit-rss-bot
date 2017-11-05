import praw, feedparser, os, time, configparser

#Initialisation
p = configparser.ConfigParser()
if not os.path.isfile("conf.ini"):
    print("No config file found!")
else:
    p.read("conf.ini")
    settings = p.__dict__['_sections'].copy()
    reddit = praw.Reddit(
        client_id=settings['Login Info']['client_id'],
        client_secret=settings['Login Info']['client_secret'],
        password=settings['Login Info']['password'],
        user_agent=settings['Login Info']['user_agent'],
        username=settings['Login Info']['username']
    )
    subreddit = reddit.subreddit(settings['RSS Info']['subreddit'])
    rss_url = settings['RSS Info']['rss_url']

#Main code
if not os.path.isfile("postedarticles.txt"):
    postedArticles = []
else:
    with open("postedarticles.txt", "r") as f:
       postedArticles = f.read()
       postedArticles = postedArticles.split("\n")
       postedArticles = list(filter(None, postedArticles))

starttime=time.time()
#in seconds
interval = settings['RSS Info']['interval']
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
    print("{0} new articles found.".format(newArticles))

    with open("postedarticles.txt", "w") as f:
        for article_id in postedArticles:
            f.write(article_id + "\n")

    time.sleep(interval - ((time.time() - starttime) % interval))

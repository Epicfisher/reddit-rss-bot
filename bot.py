import praw, feedparser, os, time

#Initialisation
reddit = praw.Reddit(
    client_id=os.environ['ID'],
    client_secret=os.environ['SECRET'],
    password=os.environ['PASSWORD'],
    user_agent=os.environ['USERAGENT'],
    username=os.environ['USERNAME']
)

debug=os.environ['PYDEBUGVAL']

subreddit = reddit.subreddit(os.environ['SUBREDDIT'])
rss_url = os.environ['RSSURL']
max_posts = os.environ['MAXPOSTS']


#if not os.path.isfile("postedarticles.txt"):
#    postedArticles = []
#else:
#    with open("postedarticles.txt", "r") as f:
#       postedArticles = f.read()
#       postedArticles = postedArticles.split("\n")
#       postedArticles = list(filter(None, postedArticles))

#postedArticles = reddit.front.new()
postedArticles = reddit.redditor('TeignmouthNews').submissions.new()

starttime=time.time()
interval = float(os.environ['INTERVAL'])
while True:
    feed = feedparser.parse(rss_url)
    print("Checking for new articles!")
    newArticles = 0
    for item in feed['items']:
        linkInPosted = False
        for articleLink in postedArticles:
            #print("Checking '" + item['link'].replace("http://", "https://") + "' and '" + articleLink.url.replace("http://", "https://") + "'")
            if item['link'].replace("http://", "https://") == articleLink.url.replace("http://", "https://"):
                linkInPosted = True
        if linkInPosted == False:
            medial_url = item['media_content'][0]['url']
            if debug == 0:
                subreddit.submit(item['title'], url=item['link'])
            else:
                print("Debug: Would have posted '" + item['title'] + "' at Link '" + item['link'] + "'")
            newArticles += 1
            time.sleep(30)
        else:
            print("Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")

    print("{0} new articles were posted.".format(newArticles))

    time.sleep(interval - ((time.time() - starttime) % interval))

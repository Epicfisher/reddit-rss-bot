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

interval = float(os.environ['INTERVAL'])
post_interval = float(os.environ['POSTINTERVAL'])

#if not os.path.isfile("postedarticles.txt"):
#    postedArticles = []
#else:
#    with open("postedarticles.txt", "r") as f:
#       postedArticles = f.read()
#       postedArticles = postedArticles.split("\n")
#       postedArticles = list(filter(None, postedArticles))

#postedArticles = reddit.front.new()
postedArticlesGenerated = reddit.redditor('TeignmouthNews').submissions.new()
postedArticles = list(postedArticlesGenerated)

#for post in postedArticles:
#    print(post.url.replace("http://", "https://"))

linkInPosted = 0

starttime=time.time()
while True:
    feed = feedparser.parse(rss_url)
    print("Checking for new articles!")
    newArticles = 0
    for item in feed['items']:
        linkInPosted = 0
        i = 0
        for articleLink in postedArticles:
            i = i + 1
        print(str(i) + " Elements in postedArticles")
        for articleLink in postedArticles:
            #print("Checking '" + item['link'].replace("http://", "https://") + "' and '" + articleLink.url.replace("http://", "https://") + "'")
            #print("Checking '" + articleLink.url + "'")
            if item['link'].replace("http://", "https://") == articleLink.url.replace("http://", "https://"):
                linkInPosted = 1
                #print(item['link'].replace("http://", "https://") + " _ IS EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
            #else:
                #print(item['link'].replace("http://", "https://") + " _ IS NOT EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
        if linkInPosted == 0:
            #medial_url = item['media_content'][0]['url']
            if debug == "0":
                subreddit.submit(item['title'], url=item['link'])
                print("Posted '" + item['title'] + "' at Link '" + item['link'] + "'")
            else:
                print("(DEBUG) Would have Posted '" + item['title'] + "' at Link '" + item['link'] + "'")
            newArticles += 1
            time.sleep(post_interval)
        else:
            if debug == "1":
                print("(DEBUG) Would have Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")
            else:
                print("Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")

    print("{0} new articles were posted. Now waiting...".format(newArticles))

    time.sleep(interval - ((time.time() - starttime) % interval))

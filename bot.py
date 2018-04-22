import praw, feedparser, os, time

#Initialisation

#Login Info
reddit = praw.Reddit(
    client_id=os.environ['ID'],
    client_secret=os.environ['SECRET'],
    password=os.environ['PASSWORD'],
    user_agent=os.environ['USERAGENT'],
    username=os.environ['USERNAME']
)

#General Settings
debug=os.environ['PYDEBUGVAL']

#RSS Info
rss_url = os.environ['RSSURL']

#Post Settings
subreddit = reddit.subreddit(os.environ['SUBREDDIT'])
interval = float(os.environ['INTERVAL'])
post_interval = float(os.environ['POSTINTERVAL'])

#postedArticlesGenerated = reddit.redditor(os.environ['USERNAME']).submissions.new()
postedArticles = list(reddit.redditor(os.environ['USERNAME']).submissions.new())

linkInPosted = False

starttime=time.time()
while True:
    feed = feedparser.parse(rss_url)
    print("Now checking for new articles!")
    newArticles = 0
    for item in feed['items']:
        linkInPosted = False
        for articleLink in postedArticles:
            #print("Checking '" + item['link'].replace("http://", "https://") + "' and '" + articleLink.url.replace("http://", "https://") + "'")
            if item['link'].replace("http://", "https://") == articleLink.url.replace("http://", "https://"):
                linkInPosted = True
                #print(item['link'].replace("http://", "https://") + " _ IS EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
            #else:
                #print(item['link'].replace("http://", "https://") + " _ IS NOT EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
        if linkInPosted == False:
            if debug == "0":
                subreddit.submit(item['title'], url=item['link'].replace("http://", "https://"))
                print("Posted '" + item['title'] + "' at Link '" + item['link'].replace("http://", "https://") + "'")
                time.sleep(post_interval)
            else:
                print("(DEBUG) Would have Posted '" + item['title'] + "' at Link '" + item['link'].replace("http://", "https://") + "'")
            newArticles += 1
        else:
            if debug == "1":
                print("(DEBUG) Would have Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")
            else:
                print("Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")

    print("{0} new articles were posted. Now waiting {1} seconds...".format(newArticles, interval))

    time.sleep(interval - ((time.time() - starttime) % interval))

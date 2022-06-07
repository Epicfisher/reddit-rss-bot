import praw, feedparser, configparser, os, time

# Initialisation
p = configparser.ConfigParser()
pExists = True
if not os.path.isfile("conf.ini"):
    print("(INIT) No config file found! This is not a fatal error assuming you have used System Environment Variables to assign your Mandatory config variables instead!")
    pExists = False
else:
    p.read("conf.ini")
    settings = p.__dict__['_sections'].copy()

def LoadConfigVariable(system_variable, header, key, mandatory, default_value=-1):
    try:
        out=os.environ[system_variable]
        print("(INIT) Loaded " + system_variable + " from System Environment Variable")
    except:
        if pExists:
            out = settings[header][key]
        else:
            if mandatory:
                print("(INIT) FATAL ERROR: Mandatory Variable " + system_variable + " Missing from Both Config File and System Environment Variable! Exiting...")
                raise SystemExit(0)
            else:
                print("(INIT) INFORMATION: Optional Variable " + system_variable + " Missing from Both Config File and System Environment Variable! Using Default Value of " + str(default_value) + "...")
                out = default_value
    return out

## Login Info
_client_id = LoadConfigVariable('REDDITRSSID', 'Login Info', 'id', True)
_client_secret = LoadConfigVariable('REDDITRSSSECRET', 'Login Info', 'secret', True)
_password = LoadConfigVariable('REDDITRSSPASSWORD', 'Login Info', 'password', True)
_user_agent = LoadConfigVariable('REDDITRSSUSERAGENT', 'Login Info', 'user_agent', True)
_username = LoadConfigVariable('REDDITRSSUSERNAME', 'Login Info', 'username', True)

reddit = praw.Reddit(
    client_id=_client_id,
    client_secret=_client_secret,
    password=_password,
    user_agent=_user_agent,
    username=_username
)

## General Settings
debug = int(LoadConfigVariable('REDDITRSSPYDEBUGVAL', 'General Settings', 'py_debug_val', False, 0))
save_posted = int(LoadConfigVariable('REDDITRSSSAVEPOSTED', 'General Settings', 'save_posted', False, 0))

## RSS Info
rss_url = LoadConfigVariable('REDDITRSSURL', 'RSS Info', 'rss_url', True)

## Post Settings
subreddit = LoadConfigVariable('REDDITRSSSUBREDDIT', 'Post Settings', 'subreddit', True)
interval = float(LoadConfigVariable('REDDITRSSINTERVAL', 'Post Settings', 'interval', False, 3600))
post_interval = float(LoadConfigVariable('REDDITRSSPOSTINTERVAL', 'Post Settings', 'post_interval', False, 30))
# Initialisation End

if save_posted:
    if not os.path.isfile("postedarticles.txt"):
        postedArticles = []
    else:
        with open("postedarticles.txt", "r") as f:
            postedArticles = f.read()
            postedArticles = postedArticles.split("\n")
            postedArticles = list(filter(None, postedArticles))

starttime=time.time()
while True:
    feed = feedparser.parse(rss_url)
    if not save_posted:
        postedArticles = list(reddit.redditor(_username).submissions.new())
    print("Now checking for new articles!")
    newArticles = 0
    for item in feed['items']:
        linkInPosted = False
        if not (save_posted and item['id'] not in postedArticles):
            for articleLink in postedArticles:
                #print("Checking '" + item['link'].replace("http://", "https://") + "' and '" + articleLink.url.replace("http://", "https://") + "'")
                if item['link'].replace("http://", "https://") == articleLink.url.replace("http://", "https://"):
                    linkInPosted = True
                    #print(item['link'].replace("http://", "https://") + " _ IS EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
                #else:
                    #print(item['link'].replace("http://", "https://") + " _ IS NOT EQUAL TO _ " + articleLink.url.replace("http://", "https://"))
        if linkInPosted == False:
            if debug == 0:
                subreddit.submit(item['title'], url=item['link'].replace("http://", "https://"))
                print("Posted '" + item['title'] + "' at Link '" + item['link'].replace("http://", "https://") + "'")
                time.sleep(post_interval)
            else:
                print("(DEBUG) Posted '" + item['title'] + "' at Link '" + item['link'].replace("http://", "https://") + "'")
            if save_posted:
                postedArticles.append(item['id'])
            newArticles += 1
        else:
            if debug == 1:
                print("(DEBUG) Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")
            else:
                print("Skipped '" + item['title'] + "' at Link '" + item['link'] + "'")

    print("{0} new articles were posted. Now waiting {1} seconds...".format(newArticles, interval))

    with open('postedarticles.txt', 'w') as f:
        for article_id in postedArticles:
            f.write(article_id + "\n")

    time.sleep(interval - ((time.time() - starttime) % interval))

# Reddit RSS Bot
A bot that checks an rss feed at intervals for unposted articles and posts them to a subreddit

## Setup
### Install requirements
```
pip3 install praw, feedparser, configparser
```

### Edit config
#### RSS Info
```
subreddit= the subreddit to post to
rss_url= url of the rss feed
interval= the seconds between each rss check
```

#### Login Info
```
client_id= client id from your app https://www.reddit.com/prefs/apps/
client_secret= client secret from your app https://www.reddit.com/prefs/apps/
password= bot account password
username= bot account username
user_agent= Anything (BotName v1.1)
```

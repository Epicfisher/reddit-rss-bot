# Modified Reddit RSS Bot
### (To Work with System Environment Variables)
A bot that checks an rss feed at intervals for unposted articles and posts them to a subreddit

## Setup
### Install requirements
To install requirements, you can either install directly from the requirements.txt file
```
pip3 install -r requirements.txt
```
Or, you can choose to install them manually
```
pip3 install praw, feedparser
```

### System Environment Config Variables
#### Login Info
```
'ID' = Client ID from your app (https://www.reddit.com/prefs/apps/)
'SECRET' = Client Secret from your app (https://www.reddit.com/prefs/apps/)
'PASSWORD' = Bot Account Password
'USERNAME' = Bot Account Username
'USERAGENT' = Can be anything (For example, name it after your bot, like "BotName v1.1")
```

#### General Settings
```
'PYDEBUGVAL' = Can be 1 or 0. If 1, the bot doesn't post anything (Default is 0)
```

#### RSS Info
```
'RSSURL' = URL of the RSS feed to use
```

#### Post Settings
```
'SUBREDDIT' = The Subreddit's name to post to
'INTERVAL' = Amount of seconds to wait between each RSS check (Default is 3600, which equates to 1 hour)
'POSTINTERVAL' = Amount of seconds to wait after each post has been made (Default is 30)
```

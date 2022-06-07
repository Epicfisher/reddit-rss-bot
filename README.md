# Modified Reddit RSS Bot

A Bot that checks an RSS Feed at intervals for unposted articles and posts them to a Subreddit.

## Features
* Portable: Queries Reddit for already posted Links without having to externally keep track
* Configurable settings allow for fine-tuning of delays between every post and RSS check
* Allows for loading of config variables via Config File or System Environment Variables

## Setup
### Install requirements
To install requirements, you can either install directly from the requirements.txt file
```
pip3 install -r requirements.txt
```
Or, you can choose to install them manually
```
pip3 install praw, feedparser, configparser
```

### Config Variables

#### Config File
You can store your Config Variables in a file called `conf.ini`.

##### Mandatory Config Variables
The following Config Variables are Mandatory, and your Bot will not start without them

###### [Login Info]
```
'id' = Client ID from your app (https://www.reddit.com/prefs/apps/)
'secret' = Client Secret from your app (https://www.reddit.com/prefs/apps/)
'password' = Bot Account Password
'username' = Bot Account Username
'user_agent' = Can be anything (For example, name it after your bot, like "BotName v1.1")
```

###### [RSS Info]
```
'rss_url' = URL of the RSS feed to use
```

###### [Post Settings]
```
'subreddit' = The Subreddit's name to post to
```

##### Optional Config Variables
The following Config Variables are not nececcary for your Bot to work, and have Default Values

###### [General Settings]
```
'py_debug_val' = Can be 1 or 0. If 1, the bot doesn't post anything [Default is 0]
'save_posted' = Can be 1 or 0. If 1, the bot saves posts to a text document [Default is 0]
```

###### [Post Settings]
```
'interval' = Amount of seconds to wait between each RSS check [Default is 3600, which equates to 1 hour]
'post_interval' = Amount of seconds to wait after each post has been made [Default is 30]
```

#### System Environment Variables
Or, as an alternative, you can choose to store your Config Variables within System Environment Variables

##### Mandatory System Environment Config Variables
The following Config Variables are Mandatory, and your Bot will not start without them

###### Login Info
```
'REDDITRSSID' = Client ID from your app (https://www.reddit.com/prefs/apps/)
'REDDITRSSSECRET' = Client Secret from your app (https://www.reddit.com/prefs/apps/)
'REDDITRSSPASSWORD' = Bot Account Password
'REDDITRSSUSERNAME' = Bot Account Username
'REDDITRSSUSERAGENT' = Can be anything (For example, name it after your bot, like "BotName v1.1")
```

###### RSS Info
```
'REDDITRSSURL' = URL of the RSS feed to use
```

###### Post Settings
```
'REDDITRSSSUBREDDIT' = The Subreddit's name to post to
```

##### Optional System Environment Config Variables
The following Config Variables are not nececcary for your Bot to work, and have Default Values

###### General Settings
```
'REDDITRSSPYDEBUGVAL' = Can be 1 or 0. If 1, the bot doesn't post anything [Default is 0]
'REDDITRSSSAVEPOSTED' = Can be 1 or 0. If 1, the bot saves posts to a text document [Default is 0]
```

###### Post Settings
```
'REDDITRSSINTERVAL' = Amount of seconds to wait between each RSS check [Default is 3600, which equates to 1 hour]
'REDDITRSSPOSTINTERVAL' = Amount of seconds to wait after each post has been made [Default is 30]
```

## Usage
The Bot can be started by running the `bot.py` file in your preferred version of Python 3

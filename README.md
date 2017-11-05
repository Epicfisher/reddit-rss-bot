# RedditRSSBot
I created this as a bot for posting news to my own subreddit but anyone can use it.

## Python Libraries
For windows:
Open up cmd and install the necessary packages
```
pip3 install praw, feedparser, configparser
```

## Config Editing
Open up conf.ini in a text editor of your choice.
Set subreddit to the subreddit you would like to post these rss feed articles.
Set rss_url to the url of the rss feed you're requesting items from.

client_id and client_secret are got from creating a script app at ``https://www.reddit.com/prefs/apps/``

password and username are the password and username to the bot account you create for the bot to use.

You can name your user_agent anything, BotName v1.1 is a suitable and preferable title.

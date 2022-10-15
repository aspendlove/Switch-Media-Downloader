# auto_twitter_download

**This script has only been tested on fedora server and I make no guarantees to it's compatibility with anything else. This software is in early alpha; It is a hobby project that I am currently working on. I make no claims to it's stability or efficiency.**

Automatically downloads any video / picture posted to a specific twitter user's timeline. 
It's intended purpose is to be run on a file storage server. On a nintendo switch, you use the built in twitter post function to post the content on a twitter account that will automatically be downloaded to the server.

**Be wary, anything you post will be visible on your twitter timeline, and open to the public. If you don't want to clutter your main twitter account you can create burner account just for this**

Example:
1. Run auto_twitter_download on a server running nextcloud, and create a cron job to run the script at boot
2. Make sure that the script runs in the working directory in which you would like the files to be stored
	1. The working directory should be in a place that nextcloud has access to, either by placing it in a certain folder or using the removable storage feature of nextcloud to point it to a folder not usually controlled by nextcloud. The removable storage feature is useful for the nextcloud snap, allowing you to use a folder in your home directory and give nextcloud access to it.
3. Insert the correct credentials for the twitter api, and give it the user id of the timeline you would like to watch
4. Run the script, it will poll the feed every minute. It pulls the last 5 tweets, so if you post more than 5 tweets in a minute the oldest will not be downloaded. It polls for the id of the last tweet, so if it detects that no new tweets have been posted then it will rest for another minute. This is to reduce system usage and API limits.
5. Post a tweet from your nintendo switch from the screenshot menu, containing a screenshot or video replay. The tweet body will be the filename. Numbers are added at the end of duplicate filenames to differentiate them, duplicates are not overwritten.
6. Wait at most a minute, and check nextcloud. Your screenshot / video will be in the preset folder.

This script is mainly a way to get screenshots and videos of your switch without having to pull out sd cards or setup a fileshare. It is very handy for sharing them with friends, especially if you can give them access to a shared nextcloud folder. The server and switch don't have to be on the same local network either, everything is sent over the internet.

# Switch Media Downloader

Automatically downloads any video / picture posted to a specific Twitter user's timeline.

When run on a file server, it will continually watch for new tweets on a specified account. When you post a tweet from your Nintendo Switch, the service will automatically download the media contained in the tweet.

This script is mainly a way to get screenshots and videos of your switch without having to pull out SD cards or set up a file share. It is very handy for sharing them with friends, especially if you can give them access to a shared Nextcloud folder.

**Be wary, anything you post will be visible on your twitter timeline, and open to the public. If you don't want to clutter your main Twitter account, you can create a burner account just for this**

## Installation

### Prerequisites 
***Thank you to these projects for providing the tools to make this project possible.***

- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [gallery-dl](https://github.com/mikf/gallery-dl)
- [Python 3](https://www.python.org/)

### Procedure

Clone the repo or download the zip and unpack it. Rename the example_config.txt file to config.txt and
fill in the required information from your twitter developer account between the quotation marks. You can find
your twitter id [here](https://tweeterid.com/).

After filling out your configuration file, run 
```
python3 switch-media-downloader.py
```
or the equivalent command to run a python 3 program for whatever operating system / configuration you run.

The service will now continue to run in the background, until it is stopped or the machine reboots.

## Notes

- The script only checks for new tweets every minute
- The script only downloads the last 5 tweets at a time, ignoring duplicates
	- If you post six or more tweets in under a minute, only the last 5 will be downloaded
- The script is designed to stay under the API limits for a free Twitter developer account

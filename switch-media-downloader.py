import os
from time import sleep
from datetime import datetime
import tweepy
import subprocess

config_file = open("config.txt", "r")


def get_configuration_from_string(input_string):
    working_tuple = input_string.partition("\"")  # remove everything before the "
    working_tuple = working_tuple[2].partition("\"")  # remove everything after the second "
    return working_tuple[0]


api_key = get_configuration_from_string(config_file.readline())
api_secrets = get_configuration_from_string(config_file.readline())
bearer_token = get_configuration_from_string(config_file.readline())
user_id = get_configuration_from_string(config_file.readline())

config_file.close()

client = tweepy.Client(bearer_token)


def download_videos(_response):
    # get filenames for all the tweets, it strips the links from the tweet body, then sets the body to the filename
    # the filenames have a maximum length of 25 characters
    # if there is a duplicate filename, then the date is added
    # videos are never downloaded twice, regardless of filename
    filename_list = []
    for index in range(len(_response.data)):
        if _response.includes["media"][index]["data"]["type"] == "video":
            tweet = _response.data[index]
            head, sep, tail = tweet.data["text"].partition("http")
            if len(head) == 0:
                head = tweet.data["id"]
            head = head[:-1][:25]
            # head = head[:25]
            for filename in filename_list:
                if filename == head:
                    head += "_" + datetime.now().strftime("%m_%d_%Y__%H:%M:%S")
            filename_list.append(head)
            # download videos, the --download-archive feature of youtube-dl ensures no duplicate downloads
            os.system("youtube-dl -f mp4 -o \"videos/" + head + ".%(ext)s\" --download-archive history.txt " +
                      tweet.data["entities"]["urls"][0]["url"])


def filename_exists(filename, path):
    for file in os.listdir(path):
        if file == filename:
            return True
    return False


def download_images(_response):
    for index in range(len(_response.data)):
        if _response.includes["media"][index]["data"]["type"] == "photo":
            file_name_old_unprocessed = subprocess.run(
                ["snap", "run", "gallery-dl", "-s", _response.data[index].data["entities"]["urls"][0]["expanded_url"]],
                stdout=subprocess.PIPE).stdout.decode('utf-8')
            head, sep, file_name_old = file_name_old_unprocessed.partition("#")
            head, sep, file_format = file_name_old_unprocessed[-5:].partition(".")
            file_name_old = file_name_old.strip()
            file_name_new, sep, tail = _response.data[index]["text"].partition("http")
            file_name_new = file_name_new.strip()
            os.system("snap run gallery-dl --download-archive image_history.txt -D ./screenshots " +
                      _response.data[index].data["entities"]["urls"][0]["expanded_url"])
            index = 1
            if filename_exists(file_name_old, "screenshots"):
                while filename_exists(file_name_new + "." + file_format.strip(), "screenshots"):
                    file_name_new += "_" + str(index)
                    index += 1
                os.rename("screenshots/" + file_name_old, "screenshots/" + file_name_new + "." + file_format.strip())


if __name__ == '__main__':
    last_newest_id = 0
    while True:
        response = client.get_users_tweets(user_id, tweet_fields=["entities"], expansions="attachments.media_keys",
                                           max_results=5)
        # a simple check to see if there are any new tweets, if not we don't need to run youtube-dl
        current_newest_id = response.meta["newest_id"]
        if current_newest_id != last_newest_id:
            download_images(response)
            download_videos(response)
        else:
            print("no new tweets")
        last_newest_id = current_newest_id
        sleep(60)

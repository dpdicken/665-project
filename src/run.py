import sys
import os
import data

def main():
    for filename in os.listdir("../resources/temp/"):
        tweets = data.read_json_data_file("../resources/temp/" + filename)
        print(filename)
        for tweet in tweets:
            print(tweet['user']['screen_name'])

if __name__ == "__main__":
    main()

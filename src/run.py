import sys
import os
import data
from model import DUWE

data_dir = "../resources/test/"

def main():
    model = DUWE()
    tweets = {}

    if __debug__:
        print("Loading data...", end="")

    for filename in os.listdir(data_dir):
        new_user = data.read_json_data_file(data_dir + filename)
        tweets.update(new_user)

    if __debug__:
        print(" Done.")

    model.train(tweets)

if __name__ == "__main__":
    main()

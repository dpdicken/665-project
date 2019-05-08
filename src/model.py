import utils
import numpy as np

from calculations import *
from datetime import datetime, timedelta
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder

class DUWE():

        def __init__(self):
            self.time_delta = timedelta(days=1)

        def train(self, data):
            if __debug__:
                print("Training DUWE model...")

            self.data = data
            self.dm = UserDocumentManager(data)
            users = self.data.keys()
            start_time = self.find_smallest_time()
            end_time = self.find_largest_time()

            print(start_time / self.time_delta)

            # Here is will we will set up data and create the embeddings at each time step
            while start_time <= end_time:
                next_time = start_time + self.time_delta
                for user in users:
                    time_step_docs = list(filter(lambda x: start_time < x['time'] and x['time'] < next_time, self.data[user]))
                    if len(time_step_docs) > 0:
                        compute_alpha_squared(self.dm, self.data, user, next_time, start_time)
                start_time = next_time

        def generate_top_k_words(self, k, time):

            # Create embeddings must be run first. We return the top k relevant
            # words for each user at time
            pass

        def find_smallest_time(self):
            stop_time = None
            for user in self.data.keys():
                user_data = self.data[user]
                for tweet in user_data:
                    if stop_time == None or tweet['time'] < stop_time:
                        stop_time = tweet['time']
            return stop_time

        def find_largest_time(self):
            stop_time = None
            for user in self.data.keys():
                user_data = self.data[user]
                for tweet in user_data:
                    if stop_time == None or tweet['time'] > stop_time:
                        stop_time = tweet['time']
            return stop_time

################################################################################

class UserDocumentManager():

    def __init__(self, data):
        users = list(data.keys())
        self.user_labels = LabelEncoder()
        self.user_labels.fit(users)

        words = utils.get_unique_words(data)

        self.word_labels = LabelEncoder()
        self.word_labels.fit(list(words))

        self.diffusion_values = defaultdict(lambda: 0)
        self.counts = np.zeros((len(words), len(users)))

    def get_user_distribution(self, user):
        pass

    def set_user_distribution(self, user, update):
        # add the passed in values from the map (update) to the correct entries in self.counts
        user_index = self.user_labels.transform([user])[0]
        for word in update.keys():
            word_label = self.word_labels.transform([word])[0]
            self.counts[word_label][user_index] += update[word]

    def count_total_word_appearences(self, user):
        # counts of word appearences over whole document set
        counts = defaultdict(int)
        user_index = self.user_labels.transform([user])[0]
        i = 0
        for word in self.counts:
            actual_word = self.word_labels.inverse_transform([i])[0]
            counts[actual_word] = word[user_index]
            i += 1
        # print("COUNTS: ", counts)
        return counts

    def get_user_diffusion(self, user):
        return self.diffusion_values[user]

    def set_user_diffusion(self, user, documents):
        # Get the average length of the docs passed in
        avg_length = len(documents[0]['text'])
        for tweet in documents:
            avg_length = (avg_length + len(tweet['text'])) / 2

        # Update users diffusion value
        self.diffusion_values[user] = (self.diffusion_values[user] + avg_length) / 2

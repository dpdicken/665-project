from collections import defaultdict
import utils
import sys

def count_appearences(documents):
        counts = defaultdict(int)
        for document in documents:
            for word in document['text'].split(" "):
                counts[word] += 1
        return counts

def compute_user_distribution_at_time(dm, data, user, t_cur, t_prev):

    if __debug__:
        print("Calculating distribution at interval ", t_cur, ", ", t_prev, " for user ", user, "...", end="")
        sys.stdout.flush()

    documents = list(filter(lambda d: t_prev < d['time'] and d['time'] <= t_cur, data[user]))
    if len(documents) == 0:
        return []

    # Count words in current time inteval document set
    counts = count_appearences(documents)
    words_count = sum(counts.values())

    # Update relevant values (i.e. total counts of words, diffusion value)
    dm.set_user_distribution(user, counts)
    dm.set_user_diffusion(user, documents)

    total_counts = dm.count_total_word_appearences(user)
    total_words_count = sum(total_counts.values())

    words = utils.get_unique_words({user : data[user]})
    e = dm.get_user_diffusion(user)
    denom = words_count + len(counts) * e
    D = []
    for word in words:
        theta = (counts[word] + e * (total_counts[word] / total_words_count)) / denom
        D.append(theta)

    if __debug__:
        print(" Done")

    return D

def g():

#
# def compute_word_occurence_in_documents(word, documents):
#     pass
#
# def compute_average_doc_length(user_documents):
#     pass
#
# # Given a set of documents at a given time and a user, compute the
# def compute_document_set_for_user(user, document_set):
#     user_documents = []
#     delta = compute_average_doc_length(user_documents)
    pass

# Used for calculating the alpha^2 parameter for a given user and time step
#  e      - Diffusion constant for user
#  d_cur  - Documents for user at current time
#  d_prev - Documents for user at previous time
#  t_cur  - Current time step
#  t_prev - Previous time step
def compute_alpha_squared(dm, data, user, t_cur, t_prev):
    distribution = compute_user_distribution_at_time(dm, data, user, t_cur, t_prev)
    # e
    # prev_distribution = dm.get_current_user_distribution(user)
    # cur_distribution =
    #
    # e * g(d_cur, d_prev) * (t_cur - t_prev)
    print(distribution)
    pass

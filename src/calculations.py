
# Used for calculating the alpha^2 parameter for a given user and time step
#  e      - Diffusion constant for user
#  d_cur  - Documents for user at current time
#  d_prev - Documents for user at previous time
#  t_cur  - Current time step
#  t_prev - Previous time step
def compute_alpha_squared(e, d_cur, d_prev, t_cur, t_prev):

    pass


def compute_word_occurence_in_documents(word, documents):
    pass

def compute_average_doc_length(user_documents):
    pass

# Given a set of documents at a given time and a user, compute the
def compute_document_set_for_user(user, document_set):
    user_documents = []
    delta = compute_average_doc_length(user_documents)
    pass

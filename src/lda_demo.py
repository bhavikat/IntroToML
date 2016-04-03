from __future__ import division, print_function
import numpy as np
import lda
import lda.datasets

#document-term matrix
X = lda.datasets.load_reuters()
print("type(X): {}".format((type(X))))
print("shape: {}\n".format(X.shape))

#vocab
vocab = lda.datasets.load_reuters_vocab()
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}\n".format(len(vocab)))

#titles for each story
titles = lda.datasets.load_reuters_titles()
print("type(titles): {}".format(type(titles)))
print("len(titles): {}".format(len(titles)))


model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
model.fit(X)

topic_word = model.topic_word_
print("type(topic_word): {}".format((type(topic_word))))
print("shape: {}".format(topic_word.shape))

#top 5 words for each probability
n = 4
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1): -1]
    print('Topic {}\n- {}'.format((i, ' '.join(topic_words))))


doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))

for n in range(5):
    sum_pr = sum(doc_topic[n,:])
    print("document: {} sum: {}".format(n, sum_pr))

#sample the most-probable topic based on titles of new stories

for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print("doc: {} topic: {}\n{}...".format(n,
                                            topic_most_pr,
                                            titles[n][:50]))
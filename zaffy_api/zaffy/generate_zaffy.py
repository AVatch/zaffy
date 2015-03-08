import random

import nltk

import img_select
import reddit

if __name__ == '__main__':
    viral = reddit.get_data()
    nouns = []

    while not nouns:
        topic = random.choice(viral)
        text = nltk.tokenize.word_tokenize(topic[0])
        tokenized = nltk.pos_tag(text)
        nouns = [s[0] for s in tokenized if s[1] == 'NN']

    noun = random.choice(nouns)
    img = img_select.pick_img(noun)

import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import nltk

from scrapers.reddit import get_data
from scrapers.img_select import pick_img
from scrapers.color_stain_filter import filt
from zaffy.models import Zaffy


@api_view(('GET',))
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def gen_zaffy(request, format=None):
    viral = None
    while not viral:
        viral = get_data()

    nouns = []
    for topic in viral:
        text = nltk.tokenize.word_tokenize(topic[0])
        tokenized = nltk.pos_tag(text)
        nouns = nouns + [s[0] for s in tokenized if s[1] == 'NN']

    failed = True
    while failed:
        try:
            noun = random.choice(nouns)

            name = noun + ' '
            for _ in range(2):
                name += random.choice(nouns) + ' '
            name = name[:-1]
            img = pick_img(noun)
            fname = filt(img)
            failed = False
        except Exception as e:
            print e
            failed = True

    Zaffy.objects.create(title=noun, media=fname, description=name)
    return Response({"topic": noun, "image": fname, "description": name})

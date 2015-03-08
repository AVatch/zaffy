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
from zaffy.models import Zaffy


@api_view(('GET',))
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def gen_zaffy(request, format=None):
    viral = get_data()
    nouns = []

    while not nouns:
        topic = random.choice(viral)
        text = nltk.tokenize.word_tokenize(topic[0])
        tokenized = nltk.pos_tag(text)
        nouns = [s[0] for s in tokenized if s[1] == 'NN']

    noun = random.choice(nouns)
    img = pick_img(noun)
    Zaffy.objects.create(title=noun, media=img)
    return Response({"topic": noun, "image": img})

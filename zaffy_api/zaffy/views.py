from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions

from zaffy.models import Zaffy
from zaffy.serializers import ZaffySerializer


class ZaffyList(generics.ListCreateAPIView):
    """
    @url: /api/v1/zaffy/
    """
    queryset = Zaffy.objects.all()
    serializer_class = ZaffySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class ZaffyDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    @url: /api/v1/zaffy/<pk>/
    """
    queryset = Zaffy.objects.all()
    serializer_class = ZaffySerializer
    authentication_classes = (authentication.SessionAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

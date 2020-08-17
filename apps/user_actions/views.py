from rest_framework import viewsets

from .models import UserFav
from .serializers import UserFavSerializer


class UserFavViewSet(viewsets.ModelViewSet):
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from authors.serializers import AuthorModelSerializer
from authors.models import Author


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all() # Сортируем всех авторов
    serializer_class = AuthorModelSerializer

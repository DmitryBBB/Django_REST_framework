from rest_framework.serializers import ModelSerializer
from authors.models import Author

""" Создание сериализатора(прослойки для вывода) """


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # можно описать только необходимые поля "first_name", ...

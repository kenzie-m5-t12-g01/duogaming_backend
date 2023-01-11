from rest_framework.test import APITestCase
from rest_framework.views import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from tests.factories.user_factories import (create_user_with_token, create_non_user_with_token)

User: AbstractUser = get_user_model()

class UserViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_user_creation_without_required_fields(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        # STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        resulted_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST sem todos os campos obrigatórios "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)

        # RETORNO JSON
        resulted_data: dict = response.json()
        expected_fields = {
            "email",
            "username",
            "password",
        }
        returned_fields = set(resulted_data.keys())
        msg = "Verifique se todas as chaves obrigatórias são retornadas ao tentar criar um usuário sem dados"
        self.assertSetEqual(expected_fields, returned_fields, msg)

class UserLoginTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users/login/"

        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_user_login_without_required_fields(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        # STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        returned_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST sem todos os campos obrigatórios "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, returned_status_code, msg)

        # RETORNO JSON
        returned_data: dict = response.json()
        expected_fields = {
            "username",
            "password",
        }
        returned_fields = set(returned_data.keys())
        msg = "Verfique se todas as chaves obrigatórias são retornadas ao tentar logar um usuário sem dados"
        self.assertSetEqual(expected_fields, returned_fields, msg)

    def test_login_success(self):
        register_data = {
            "username": "matheuzin",
            "email": "matheus@kenzie.com.br",
            "password": "131354545",
        }
        User.objects.create_user(**register_data)
        login_data = {
            "username": "matheuzin",
            "password": "131354545",
        }

        # STATUS CODE
        response = self.client.post(self.BASE_URL, data=login_data, format="json")
        expected_status_code = status.HTTP_200_OK
        returned_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, returned_status_code, msg)

        # RETORNO TOKEN
        expected_keys = {"access", "refresh"}
        returned_keys = set(response.json().keys())
        msg = (
            "Verifique se o token está sendo retornado corretamente "
            + f"em `{self.BASE_URL}`"
        )

        self.assertSetEqual(expected_keys, returned_keys, msg)

    def test_login_with_wrong_credentials(self):
        login_data = {
            "username": "matheuszon",
            "password": "11111111111111111",
        }

        # STATUS CODE
        response = self.client.post(self.BASE_URL, data=login_data, format="json")
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        returned_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, returned_status_code, msg)

        # RETORNO JSON
        returned_data: dict = response.json()
        expected_data = {"detail": "No active account found with the given credentials"}
        msg = "Verifique se a mensagem de credenciais inválidas está correta"
        self.assertDictEqual(expected_data, returned_data, msg)
    
class UserGetTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/users/%s/"

        cls.user, cls.user_token = create_user_with_token()

        cls.non_user, cls.non_user_token = create_non_user_with_token()

        # UnitTest Longer Logs
        cls.maxDiff = None
    
    def test_get_user_info_without_token(self):
        base_url = self.BASE_URL % self.user.id
        response = self.client.get(base_url)

        # STATUS CODE
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code

        msg = (
            "Verifique se o status code retornado do POST sem token "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)
    
    def test_if_a_user_can_get_another_user_profile_info(self):
        base_url = self.BASE_URL % self.non_user.id
        user_token = str(self.user_token.access_token)
        # STATUS CODE
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
        response = self.client.get(base_url)
        # ipdb.set_trace()
        expected_status_code = status.HTTP_200_OK
        returned_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do GET "
            + f"em `{base_url}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, returned_status_code, msg)

        # RETORNO JSON
        expected_keys = {
            "id",
            "username",
            "email",
            "country",
            "is_active",
            "created_at",
            "updated_at",
            "is_superuser",
            "ads",
        }
        returned_keys = set(response.json().keys())
        msg = (
            "Verifique se as chaves corretas estão sendo retornadas em "
            + f"em `{base_url}`"
        )

        self.assertSetEqual(expected_keys, returned_keys, msg)
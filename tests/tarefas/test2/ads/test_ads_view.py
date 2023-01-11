from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories.ads_factories import create_ads_with_su
from tests.factories.user_factories import (create_non_user_with_token, create_user_with_token)
from tests.factories.game_factories import create_game

class AdsViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        template_url = "api/games/%s/ads/"

        cls.game = create_game()
        """ cls.ads = create_ads_with_su() """
        cls.BASE_URL = template_url % "52ec13dc-0faf-45b9-940d-16ac4b4c7ed2"

        cls.maxDiff = None

    def test_ads_creation_with_wrong_uuid(self):
        _, token = create_user_with_token()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(token.access_token))

        response = self.client.post(self.BASE_URL, data={}, format="json")

        # STATUS CODE
        expected_status_code = status.HTTP_404_NOT_FOUND
        resulted_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST sem todos os campos obrigatórios "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)
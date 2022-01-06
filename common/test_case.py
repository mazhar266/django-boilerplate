from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient

from core.tests import UserFactory


#pylint: disable=invalid-name
class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.pharmacy = UserFactory(is_pharmacy=True)
        self.admin = UserFactory(is_staff=True)

    def assertCreated(self, request):
        self.assertEqual(request.status_code, 201)

    def assertSuccess(self, request):
        self.assertEqual(request.status_code, 200)

    def assertDeleted(self, request):
        self.assertEqual(request.status_code, 204)

    def assertBadRequest(self, request):
        self.assertEqual(request.status_code, 400)

    def assertUnAuthorized(self, request):
        self.assertEqual(request.status_code, 401)

    def assertPermissionDenied(self, request):
        self.assertEqual(request.status_code, 403)

    def assertNotFound(self, request):
        self.assertEqual(request.status_code, 404)

    def assertMethodNotAllowed(self, request):
        self.assertEqual(request.status_code, 405)

    def create_image(self, size=(50, 50)):
        file_ = BytesIO()
        image = Image.new('RGBA', size=size, color=(155, 0, 0))
        image.save(file_, 'png')
        file_.seek(0)
        mock_image = SimpleUploadedFile(
            name='test_image.png',
            content=file_.read(),
            content_type='image/png'
        )
        return mock_image

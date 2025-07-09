from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass456'
        )

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser2',
            'password': 'testpass456'
        })
        self.assertEqual(response.status_code, 302)  # redirect

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser2', password='testpass456')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)



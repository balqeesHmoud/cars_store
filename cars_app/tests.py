from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Car

class CarModelTestCase(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            model='Model X',
            brand='Brand Y',
            price=50000,
            is_bought=False,
            buyer=None,
            buy_time=None
        )

    def test_string_representation(self):
        self.assertEqual(str(self.car), f'{self.car.brand} {self.car.model}')

    def test_model_fields(self):
        self.assertEqual(self.car.model, 'Model X')
        self.assertEqual(self.car.brand, 'Brand Y')
        self.assertEqual(self.car.price, 50000)
        self.assertEqual(self.car.is_bought, False)
        self.assertIsNone(self.car.buyer)
        self.assertIsNone(self.car.buy_time)

class CarViewsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a car instance
        self.car = Car.objects.create(
            model='Model X',
            brand='Brand Y',
            price=50000,
            is_bought=False,
            buyer=None,
            buy_time=None
        )

    def test_car_list_view(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars_app/car_list.html')
        self.assertContains(response, 'Car List')
        self.assertContains(response, self.car.brand)

    def test_car_detail_view(self):
        response = self.client.get(reverse('car_detail', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars_app/car_detail.html')
        self.assertContains(response, self.car.model)
        self.assertContains(response, self.car.price)

    def test_car_create_view(self):
        response = self.client.post(reverse('car_create'), {
            'model': 'Model Y',
            'brand': 'Brand Z',
            'price': 60000,
            'is_bought': False,
            'buyer': '',
            'buy_time': ''
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(Car.objects.filter(model='Model Y').exists())

    def test_car_update_view(self):
        response = self.client.post(reverse('car_update', kwargs={'pk': self.car.pk}), {
            'model': 'Model X Updated',
            'brand': 'Brand Y Updated',
            'price': 55000,
            'is_bought': True,
            'buyer': 'John Doe',
            'buy_time': timezone.now()
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful update
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Model X Updated')

    def test_car_delete_view(self):
        response = self.client.post(reverse('car_delete', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful deletion
        self.assertFalse(Car.objects.filter(pk=self.car.pk).exists())

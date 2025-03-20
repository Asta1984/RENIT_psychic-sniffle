from django.urls import reverse
from rest_framework.test import APITestCase
from .models import ProductUnavailability  # Add missing model import

class UnavailabilityTests(APITestCase):
    def test_create_unavailability(self):
        url = reverse('product-unavailability', kwargs={'product_id': 1})
        data = {'dates': ['2024-01-01', '2024-01-02'], 'reason': 'Maintenance'}
        response = self.client.post(url, data, format='json')
        
        # Assert the response status code
        self.assertEqual(response.status_code, 201)
        
        # Assert the number of created entries
        self.assertEqual(ProductUnavailability.objects.count(), 2)
from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from doctors.models import Doctor
from bookings.models import Booking

class BookingTestCase(TestCase):

    def setUp(self):
        # Create a doctor with a booking capacity of 10 (for example)
        self.doctor = Doctor.objects.create(name="Dr. Smith", book_capacity=10, current_bookings=0)
        
        # Create 100 users with unique emails
        self.users = [
            CustomUser.objects.create_user(username=f'user_{i}', email=f'user_{i}@example.com', password='password')
            for i in range(100)
        ]
        
        self.client = Client()

    def test_bulk_booking(self):
        url = reverse('get_ticket')  # Assuming your url pattern is named 'get_ticket'
        
        responses = []
        for user in self.users:
            response = self.client.post(url, {
                'userId': user.id,
                'doctorId': self.doctor.id
            }, content_type='application/json')
            responses.append(response)
        
        # Assertions to check the expected outcomes
        success_count = 0
        no_slots_count = 0
        for response in responses:
            if response.status_code == 201:
                success_count += 1
            elif response.status_code == 400 and 'No available booking slots' in response.json().get('message'):
                no_slots_count += 1

        # The first 10 bookings should be successful
        self.assertEqual(success_count, self.doctor.book_capacity)
        
        # The remaining 90 bookings should fail due to no available slots
        self.assertEqual(no_slots_count, 100 - self.doctor.book_capacity)

        # Verify that the doctor's current bookings match the book capacity
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.current_bookings, self.doctor.book_capacity)

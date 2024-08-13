from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bookings.models import Booking
from users.models import CustomUser
from doctors.models import Doctor
import json

@csrf_exempt
def get_ticket(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        user_id = data.get('userId')
        doctor_id = data.get('doctorId')
        
        # Check if doctorId is provided, return an error if not
        if not doctor_id:
            return JsonResponse({'status': 'failed', 'message': 'doctorId is required'}, status=400)
        
        try:
            user = CustomUser.objects.get(id=user_id)
            doctor = Doctor.objects.get(id=doctor_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'failed', 'message': 'User not found'}, status=404)
        except Doctor.DoesNotExist:
            return JsonResponse({'status': 'failed', 'message': 'Doctor not found'}, status=404)
        
        # Check if the user has already booked this doctor
        if Booking.objects.filter(user=user, doctor=doctor).exists():
            return JsonResponse({'status': 'failed', 'message': 'User has already booked this doctor'}, status=400)
        
        # Check if the doctor has available booking capacity
        if doctor.current_bookings >= doctor.book_capacity:
            return JsonResponse({'status': 'failed', 'message': 'No available booking slots'}, status=400)
        
        # Create the booking
        Booking.objects.create(user=user, doctor=doctor)
        doctor.current_bookings += 1
        doctor.save()

        return JsonResponse({'status': 'success', 'message': 'Booking successful'}, status=201)
    
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=405)


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Scooter, Booking
from dateutil.parser import parse
import pytz

def search_results(request):
    if request.method == 'POST':
        start_datetime = parse(request.POST.get('start_datetime'))
        end_datetime = parse(request.POST.get('end_datetime'))
        
        # Store form data in session variables
        request.session['start_datetime'] = start_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        request.session['end_datetime'] = end_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        return redirect('scooter_list')
    return render(request, 'rent.html')

def scooter_list(request):
    start_datetime = parse(request.session.get('start_datetime'))
    end_datetime = parse(request.session.get('end_datetime'))

    # Exclude scooters that are booked during the selected time
    booked_scooters = Booking.objects.filter(start_datetime__lte=end_datetime, end_datetime__gte=start_datetime).values_list('scooter', flat=True)
    scooters = Scooter.objects.exclude(id__in=booked_scooters)
    
    return render(request, 'scooterlist.html', {'scooters': scooters})

def pick_scooter(request):
    if request.method == 'POST':
        scooter_name = request.POST.get('scooter_name')
        request.session['selected_scooter'] = scooter_name
        return render(request, 'form.html', {'scooter_name': scooter_name})


def booking_success(request):
    return render(request, 'bookingsuccess.html')



def book_scooter(request):
    if request.method == 'POST':
        try:
            # Extract form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile_number = request.POST.get('mobile_number')
            permanent_address = request.POST.get('permanent_address')
            id_proof_type = request.POST.get('id_proof_type')
            id_proof_image = request.FILES.get('id_proof_image')
            id_proof_number = request.POST.get('id_proof_number')
            rider_image = request.FILES.get('rider_image')
            scooter_name = request.session.get('selected_scooter')
            
            # Extract booking period
            start_datetime = parse(request.session.get('start_datetime'))
            end_datetime = parse(request.session.get('end_datetime'))

            # Get the selected scooter
            scooter = Scooter.objects.get(name=scooter_name)

            # Create a new Booking
            booking = Booking(
                name=name,
                email=email,
                mobile_number=mobile_number,
                permanent_address=permanent_address,
                id_proof_type=id_proof_type,
                id_proof_image=id_proof_image,
                id_proof_number=id_proof_number,
                rider_image=rider_image,
                scooter=scooter,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
            )
            booking.save()
        
            return redirect('booking_success')

        except Exception as e:
            print(str(e))
            return render(request, 'book_error.html', {'error': 'Book Error'})


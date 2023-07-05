from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Car, Booking
from django.core.mail import send_mail

# Create your views here.


def allProdCat(request, c_slug=None):
    c_page = None
    cars_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        cars_list = Car.objects.all().filter(category=c_page, availability=True)
    else:
        cars_list = Car.objects.all().filter(availability=True)

    paginator = Paginator(cars_list, 6)

    try:
        page_num = int(request.GET.get('page', '1'))
    except:
        page_num = 1
    try:
        cars = paginator.page(page_num)
    except(EmptyPage, InvalidPage):
        cars = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'category': c_page, 'cars': cars})


def carDetail(request, c_slug, car_slug):
    try:

        car = Car.objects.get(category__slug=c_slug, slug=car_slug)

    except Exception as e:
        raise e
    return render(request, 'car.html', {'car': car})


def allCars(request):
    allcars = Car.objects.all()
    pagin = Paginator(allcars, 6)
    page_num = request.GET.get('page', 1)
    try:
        allcars = pagin.page(page_num)
    except (EmptyPage, InvalidPage):
        allcars = pagin.page(pagin.num_pages)

    return render(request, 'allcars.html', {'allcars': allcars})


def customer_care(request):
    return render(request, 'customer_care.html')

def thank(request):
    return render(request, 'thank.html')


def booking(request, c_slug, car_slug):
    car = Car.objects.get(category__slug=c_slug, slug=car_slug)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        district = request.POST['district']
        date = request.POST['date']
        car_name = request.POST['car_option']

        car = Car.objects.get(name=car_name)

        booking = Booking(name=name, email=email, phone=phone,
                          district=district, date=date, car=car)
        booking.save()

        return redirect('carapp:thank')

    return render(request, 'booking.html', {'car': car})




def send_email_notification(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        district = request.POST.get('district')
        date = request.POST.get('date')
        car_name = request.POST.get('car_option')

        subject = 'Booking Notification'
        message = 'Hi Admin,\n\nA new booking has been made.\n\nName: {}\nEmail: {}\nPhone: {}\nDistrict: {}\nDate: {}\nCar: {}'.format(name, email, phone, district, date, car_name,)
        from_email = 'amj.amaljoy@gmail.com'
        recipient_list = ['www.ardrapraj95@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'booking.html')


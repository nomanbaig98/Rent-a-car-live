from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin

from  . import models
from django.views.generic import CreateView, TemplateView,ListView, DetailView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin






class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class HomeView(TemplateView):
    template_name = 'accounts/home.html'


class CarListView(ListView):
    model = models.Car
    template_name = 'accounts/car_list.html'


    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        cars = models.Car.objects.filter(is_available=True)
        context['cars'] = cars

        return context


class CarDetailView(FormMixin, DetailView):
    model = models.Car
    template_name = 'accounts/car_details.html'
    form_class = forms.BookingForm


    def get_success_url(self):
        return reverse('car-details', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

        else:
            return  self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(CarDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['form'] = forms.BookingForm(initial={'post' : self.object})
        return context





    class BookingView(LoginRequiredMixin, CreateView):
        model = models.Bookings
        fields = ['car', 'booking_start_date', 'booking_end_date']


        def get_car(self):
           car_pk = self.kwargs['car_pk']
           car = models.Car.objects.get(pk=car_pk)

           return car

        def get_context_data(self, **kwargs):
            context = super(BookingView, self).get_context_data(**kwargs)
            context['car'] = self.get_car()

            return context

        def form_valid(self, form):
            new_booking = form.save(commit=False)
            new_booking.car = self.get_car()

            new_booking.is_approved = False
            new_booking.save()

            return super(BookingView, self).form_valid(form)

        def get_success_url(self):
            car = self.get_car()
            car_details_page_url = car.get_absolute_url()

            return '{}?booking-success=1'.format(car_details_page_url)



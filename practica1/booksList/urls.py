from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Author, Book, Genere

urlpatterns = [
    url(r'^$', dashboard), # Entre parentesis sera un parametre
    # El + es una vez o mas
    # [a-zA-Z0-9]+ --> \w+ quiere decir que no este en blanco
    # \w+.\w+ una palabra.otrapalabra
    url(r'^$', mainpage),
    url(r'^admin/', include(admin.site.urls)),
]
"""urlpatterns = [
    # List latest 5 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            template_name='principal.html'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^bookList/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Restaurant,
            template_name='myrestaurants/form.html',
            form_class=RestaurantForm),
        name='restaurant_edit'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Dish,
            template_name='myrestaurants/form.html',
            form_class=DishForm),
        name='dish_edit'),

    # Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
]"""
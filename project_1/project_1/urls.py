from django.contrib import admin
from django.urls import path, include
# from views import contact
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("first_app/", include("first_app.url")),
    path("second_app/", include("second_app.url")),
    path('contact/', views.contact)
]

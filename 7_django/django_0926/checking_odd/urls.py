from django.urls import path
from . import views

urlpatterns = [
    path("checking_odd/<int:number>/", views.checking_odd),
    path("calculate/<int:number_a>/<int:number_b>", views.calculate),
    path("animal/", views.animal),
    path("result/", views.result),
    path("lorem/", views.lorem),
    path("ipsum/", views.ipsum),
    path("", views.root),
]
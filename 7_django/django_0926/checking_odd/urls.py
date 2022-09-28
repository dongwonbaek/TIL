from django.urls import path
from . import views

app_name = "checking"

urlpatterns = [
    path("checking_odd/<int:number>/", views.checking_odd, name="odd"),
    path("calculate/<int:number_a>/<int:number_b>", views.calculate, name="calculate"),
    path("animal/", views.animal, name="animal"),
    path("result/", views.result, name="result"),
    path("lorem/", views.lorem, name="lorem"),
    path("ipsum/", views.ipsum, name="ipsum"),
    path("", views.root, name="root"),
]

from django.urls import path
from .views import VisitorView, StaffMemberView, DrinkView, VisitorDetailView, VisitorDrinkView
from django.conf import settings

urlpatterns = [
path('visitor/', VisitorView.as_view()),
path('staff_member/', StaffMemberView.as_view()),
path('drink/', DrinkView.as_view()),
path('visitor_details/', VisitorDetailView.as_view()),
path('visitor_drink/', VisitorDrinkView.as_view()),
]

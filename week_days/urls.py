from django.urls import path
from week_days import views

urlpatterns = [
    path("week_days/", views.WeekDayView.as_view()),
    path("week_days/<int:id>", views.WeekDayDetailView.as_view())
]
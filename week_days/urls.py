from week_days import views
from django.urls import path

urlpatterns = {
    path("week_days/", views.WeekDayListView.as_view())
}

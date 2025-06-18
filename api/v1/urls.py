from api.v1 import (
    ArtistListView,
    ArtistView,
    EventListView,
    EventView,
    TourListView,
    TourView,
    WelcomeView,
    BookingViewSet,
)
from django.urls import path

app_name = "api"

urlpatterns = [
    path("welcome/", WelcomeView.as_view(), name="index"),
    # artist
    path("artist-list/", ArtistListView.as_view(), name="artist-list"),
    path(
        "artist/<str:object_id>/",
        ArtistView.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="artist-detail",
    ),
    # event
    path("event-list/", EventListView.as_view(), name="event-list"),
    path(
        "event/<str:object_id>/",
        EventView.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="event-details",
    ),
    # tours
    path("tour-list/", TourListView.as_view(), name="tour-list"),
    path(
        "tour/<str:object_id>/",
        TourView.as_view({"get": "retrieve"}),
        name="tour-detail",
    ),
    # booking
    path(
        "booking/create/",
        BookingViewSet.as_view({"post": "create"}),
        name="booking-create",
    ),
]

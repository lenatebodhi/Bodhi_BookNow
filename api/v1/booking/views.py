from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from book_now.models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()  # Optional, but recommended for DRF tools

    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()
            data["user_id"] = request.user.id  # auto-bind user from JWT if needed

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            booking = serializer.save()

            return Response(
                {"message": "Booking created successfully", "results": self.get_serializer(booking).data},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"message": f"Something went wrong: {str(e)}", "status": "error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

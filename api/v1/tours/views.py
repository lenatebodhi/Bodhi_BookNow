from book_now.models import Tours
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated  # ✅ Require login
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from utils.paginator import CustomPagination  # Optional

from .serializers import TourSerializer


class TourListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TourSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Tours.objects.filter(is_active=True).order_by("-id")

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error_message:
            return Response(
                {
                    "message": f"Something went wrong: {error_message}",
                    "status": "error",
                    "statusCode": HTTP_500_INTERNAL_SERVER_ERROR,
                },
                status=HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TourView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TourSerializer

    def get_queryset(self):
        return Tours.objects.filter(is_active=True).order_by("-id")

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(self.get_queryset(), object_id=kwargs.get("object_id"))
            serializer = self.serializer_class(instance)
            message = "Tour detail view retrieved successfully"
            return Response({"results": serializer.data, "message": message}, status=HTTP_200_OK)

        except Exception as error_message:
            return Response(
                {
                    "message": f"Something went wrong: {error_message}",
                    "status": "error",
                    "statusCode": HTTP_500_INTERNAL_SERVER_ERROR,
                },
                status=HTTP_500_INTERNAL_SERVER_ERROR,
            )

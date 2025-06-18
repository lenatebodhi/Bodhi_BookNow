from book_now.models import Artist
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated  # ✅ Require login
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from utils.paginator import CustomPagination  # Optional, if using custom pagination

from .serializers import ArtistSerializer


class ArtistListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Artist.objects.filter(is_active=True).order_by("-id")

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


class ArtistView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.filter(
            is_active=1,
        ).order_by("-id")
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """ """
        try:
            instance = get_object_or_404(self.get_queryset(), object_id=kwargs.get("object_id"))
            serializer = self.serializer_class(instance)
            message = "Detail Page view Listed successfully"
            return Response({"results": serializer.data, "message": message}, status=HTTP_200_OK)

        except Exception as error_message:
            response_data = {
                "message": f"Something went wrong: {error_message}",
                "status": "error",
                "statusCode": HTTP_500_INTERNAL_SERVER_ERROR,
            }
            return Response(response_data, status=HTTP_500_INTERNAL_SERVER_ERROR)

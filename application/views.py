from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import Video, News
from .serializers import VideoCreateListSerializer, NewsCreateListSerializer
from .utils import ListPagination
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT


class VideoCreateListView(GenericAPIView, ListModelMixin):
    queryset = Video.objects.order_by("-created_at")
    serializer_class = VideoCreateListSerializer
    pagination_class = ListPagination

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Video created successfully!"}, status=HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class VideoDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        video_id = kwargs.get("id")
        message, status_code = "", HTTP_204_NO_CONTENT
        try:
            video_obj = Video.objects.get(pk=video_id)
            video_obj.delete()
            message = "Video has been deleted successfully"

        except ObjectDoesNotExist as e:
            message = str(e)
            status_code = HTTP_404_NOT_FOUND
        finally:
            return Response({"message": message}, status=status_code)


class NewsCreateListView(GenericAPIView, ListModelMixin):
    queryset = News.get_queryset()
    serializer_class = NewsCreateListSerializer
    pagination_class = ListPagination

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "News created successfully!"}, status=HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        news_id = kwargs.get("id")
        message, status_code = "", HTTP_204_NO_CONTENT
        try:
            news_obj = News.objects.get(pk=news_id)
            news_obj.delete()
            message = "News has been deleted successfully"
        except ObjectDoesNotExist as e:
            message = str(e)
            status_code = HTTP_404_NOT_FOUND
        finally:
            return Response({"message": message}, status=status_code)


class TrendingListView(APIView):
    def get(self, request, *args, **kwargs):
        news_queryset = News.get_queryset()[:4]
        news_serializer = NewsCreateListSerializer(news_queryset, many=True).data
        video_queryset = Video.get_queryset()[:4]
        video_serializer = VideoCreateListSerializer(video_queryset, many=True).data
        return Response({"news": news_serializer, "videos": video_serializer})

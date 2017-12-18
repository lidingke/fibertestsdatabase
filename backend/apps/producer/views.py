from django.shortcuts import render
from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
# from rest_framework.filters import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from producer.serializers import ResultSerializer
from producer.models import Result



class ResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    search_fields = ('owner')
    ordering_fields = ('-id')


class ResultListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    测试结果列表页, 分页， 搜索， 过滤， 排序
    """
    # mixins.RetrieveModelMixin,
    # throttle_classes = (UserRateThrottle, )
    queryset = Result.objects.all()

    serializer_class = ResultSerializer
    pagination_class = ResultPagination
    # authentication_classes = (TokenAuthentication, )
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = ResultFilter
    search_fields = ('owner', 'instrument')
    ordering_fields = ('id',)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.click_num += 1
    #     instance.save()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
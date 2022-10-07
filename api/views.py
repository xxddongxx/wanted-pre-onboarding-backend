from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from api import serializers
from api.models import Company, JobPost


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer

class JobPostViewSet(viewsets.ViewSet):
    queryset = JobPost.objects.all()
    serializer_class = serializers.JobPostCreateSerializer

    def create(self, request):
        serializer = serializers.JobPostCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        queryset = JobPost.objects.all()
        serializer = serializers.JobPostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = JobPost.objects.all()
        jobPost = get_object_or_404(queryset, pk=pk)
        serializer = serializers.JobPostRetrieveSerializer(jobPost)

        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = JobPost.objects.all()
        jobPost = get_object_or_404(queryset, pk=pk)

        serializer = serializers.JobPostUpdateserializer(jobPost, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = JobPost.objects.all()
        jobPost = get_object_or_404(queryset, pk=pk)
        jobPost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


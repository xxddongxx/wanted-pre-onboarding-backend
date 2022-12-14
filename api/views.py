from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics, filters
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api import serializers
from api.models import Company, JobPost, User, Application

import io

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

        companyNo = jobPost.company.pk
        anotherJobPosts = JobPost.objects.filter(company=companyNo).exclude(pk=pk).values_list('pk', flat=True)

        json = JSONRenderer().render(serializer.data)

        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)

        data["anotherPosts"] = anotherJobPosts

        return Response(data)

    def update(self, request, pk=None):
        queryset = JobPost.objects.all()
        jobPost = get_object_or_404(queryset, pk=pk)

        serializer = serializers.JobPostUpdateSerializer(jobPost, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = JobPost.objects.all()
        jobPost = get_object_or_404(queryset, pk=pk)
        jobPost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ApplicationViewSet(viewsets.ViewSet):
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def list(self, request):
        queryset = Application.objects.all()
        serializer = serializers.ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        userPk = request.data['user']

        serializer = serializers.ApplicationSerializer(data=request.data)

        if serializer.is_valid():
            if Application.objects.filter(user=userPk):
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Application.objects.all()
        application = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ApplicationSerializer(application)

        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Application.objects.all()
        application = get_object_or_404(queryset, pk=pk)

        serializer = serializers.ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Application.objects.all()
        application = get_object_or_404(queryset, pk=pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchKeywordkViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = serializers.JobPostListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['company__name', 'position', 'stack']

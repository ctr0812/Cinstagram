import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request,"cinstagram/main.html",context=dict(feeds=feed_list))

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        from Cinstagram.settings import MEDIA_ROOT
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')

        Feed.objects.create(image=image,content=content,user_id = "tim_climb97",profile_image="https://timbucket0812.s3.ap-northeast-2.amazonaws.com/291103907_558554339267389_8656762225897347722_n.jpg",like_count=0)

        return Response(status=200)
import os
from django.core.files import File

class PathToFileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ここでPath形式のDataをFile形式に変換する処理を行う
        if 'video_path' in request.POST:
            path = request.POST.get('video_path')
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    request.FILES['video_file'] = File(f)

        response = self.get_response(request)
        return response

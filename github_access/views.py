from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from hackathon.models import UserProfile 
import json

@login_required
@require_http_methods(["GET", "POST"])
def get_from_db_or_post_to_db_github_access_token(request): # 関数名を役割に合わせて変更

    user = request.user

    # GETリクエスト：DBにトークンがあるか「確認」する役割
    if request.method == 'GET':
        try:
            github_access_token = user.userprofile.github_access_token

            # トークンがDBに存在し、空でない場合
            if github_access_token:
                return JsonResponse({'exists': True, 'token': github_access_token})
            # プロフィールはあるが、トークンが空の場合
            else:
                return JsonResponse({'exists' : False, 'message': 'nothing token'})
            
        except UserProfile.DoesNotExist:
            # UserProfileモデル自体が存在しない場合
            return JsonResponse({'exists': False, 'message': 'nothing profile'})

    # POSTリクエスト：クライアントから送られてきたトークンを「格納」する役割
    elif request.method == 'POST':
        try:
            # リクエストの本文(body)からJSONデータを読み込む
            data = json.loads(request.body)
            token = data.get('github_access_token')

            # トークンが送られてきているかチェック
            if not token:
                return JsonResponse({'status': 'error', 'message': 'no reserve access token'}, status=400)

            # UserProfileを更新または新規作成してトークンを保存
            UserProfile.objects.update_or_create(
                user=user,
                defaults={'github_access_token': token}
            )
            
            return JsonResponse({'status': 'success', 'message': 'saved token','token': token}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'invalid json'}, status=400)
from django.urls import path
from . import views #同じディレクトリにあるviews.pyをインポート

app_name = 'github_access'

# このアプリで使うURLパターンをリストに記述します
urlpatterns = [
    path('token/', views.get_from_db_or_post_to_db_github_access_token, name='github_token'),
]
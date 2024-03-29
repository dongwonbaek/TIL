from django.urls import path
from . import views

"""
메인: 게시글의 목록(/posts/) / 게시글 상세
작성: 글을 작성하는 페이지(/posts/new) / 작성 완료
수정: 글을 수정하는 페이지 / 수정 완료
삭제: 글 삭제 완료
"""
app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete"),
]

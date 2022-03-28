from django.urls import path, include

from rest_framework.routers import DefaultRouter

from questions.api import views

router = DefaultRouter()
router.register(r"questions", views.QuestionViewSet)

urlpatterns = [

    path('', include(router.urls)),

    path('questions/<slug:slug>/answer/', views.AnswerCreateApiView.as_view(), name='anser_create'),
    path('questions/<slug:slug>/answers/', views.AnswerListApiView.as_view(), name='answer_list'),
    path('answer/<int:pk>/', views.AnswerRetrieveUpdateDestroyAPIView.as_view(), name='update-delete-answers'),
    path('answer/<int:pk>/like/', views.AnswerLikeAPIView.as_view(), name='answer-like'),

]


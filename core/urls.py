from django.urls import path
from core.views import SignUpView, ProfileView, ActivateAccount

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]
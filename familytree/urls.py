from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from familytree.views import *

urlpatterns = [
    path('user/', MyUserView.as_view()),
    path('user/<int:pk>/', MyUserView.as_view()),
    path('parent/', MyParentsView.as_view()),
    path('parent/<int:user_id>/', MyParentsView.as_view()),
    path('sibling/', MySiblingView.as_view()),
    path('sibling/<int:user_id>/', MySiblingView.as_view()),
    path('children/', MyChildrenView.as_view()),
    path('children/<int:user_id>/', MyChildrenView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

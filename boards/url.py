
from django.urls import path 
from . import views              # النقطة تشير الى نفس الفولدر
urlpatterns = [
    path('',views.home,name='home'),  
    path('about/',views.about,name='about'),
    path('boards/<int:board_id>/',views.board_topics,name='board_topics'),
    path('boards/<int:board_id>/new/',views.new_topic,name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/',views.topic_posts,name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/replay/',views.replay_topic,name='replay_topic'),

    
]
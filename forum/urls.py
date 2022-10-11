from django.urls import path, include

from . import views

app_name = 'forum'

urlpatterns = [
	path('forum/', views.index, name='index'),
	path('forum/discussion/<str:slug>', views.discussion, name='discussion'),
	path('forum/<str:cat_slug>', views.forum_live, name='forum_live'),
	path('post_reply/', views.post_reply, name='post_reply'),
	path('reply_reply/', views.reply_reply, name='reply_reply'),
	path('create_disc/', views.create_disc, name='create_disc'),
	path('owner_post_delete/', views.owner_post_delete, name='owner_post_delete'),
	path('add_claps/', views.add_claps, name='add_claps'),

]

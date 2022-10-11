from django.contrib import admin

from forum.models import Forum, Discussion




@admin.register(Forum)
class  ForumAdmin(admin.ModelAdmin):
	list_display = ('id', 'topic', 'cat_slug', 'status', 'created')
	prepopulated_fields = {'cat_slug': ('topic',)}

	# Restrict staff users to only change their own posts
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser or request.user.groups.filter(name='forum').exists():
			return qs
		return qs.filter(author=request.user)


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
	list_display = ('id', 'forum', 'title', 'author_id', 'author', 'status', 'parent')
	prepopulated_fields = {'slug': ('title',)}

	# Restrict staff users to only change their own posts

	# To restrict specific groups add:
	# or request.user.groups.filter(name='groupname').exists()
	# below request.user.is_superuser statement

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(author=request.user)


	def save_form(self, request, form, change):
		obj = super(DiscussionAdmin, self).save_form(request, form, change)
		if not change:
			obj.author = request.user
		return obj
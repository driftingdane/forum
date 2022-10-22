from django.db import models

# parent model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from tinymce.models import HTMLField

from core import settings


class Forum(models.Model):
    class NewManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    topic = models.CharField(max_length=300)
    status = models.CharField(max_length=10, choices=options, default='draft')
    cat_slug = models.SlugField(max_length=250, blank=True, null=True, unique=True, allow_unicode=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    class Meta:
        get_latest_by = ['-created', ]
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('forum:forum_live', args=[self.cat_slug])

    def __str__(self):
        return str(self.id) + " " + self.topic


# child model
class Discussion(models.Model):
    class NewManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies',
                               related_query_name='published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, related_name='forums', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    discuss = HTMLField()
    status = models.CharField(max_length=10, choices=options, default='published')
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True, allow_unicode=True)
    publish = models.DateTimeField(default=timezone.now)
    claps = models.BigIntegerField(default=0)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    class Meta:
        get_latest_by = ['-publish', ]
        ordering = ('publish',)

    def get_absolute_url(self):
        return reverse('index:discussion', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

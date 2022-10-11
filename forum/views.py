from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Forum, Discussion


def all_forums(request):
    all_forums = Forum.objects.filter(forums__parent__isnull=True, status="published").distinct()
    return all_forums


def forum_live(request, cat_slug):
    list_forum_post = Forum.objects.filter(cat_slug=cat_slug, status="published").order_by('-id')
    list_forums = all_forums(request).distinct().order_by("-id")
    ct_slug = cat_slug.replace("-", " ")
    print(list_forum_post.get())
    data = {
        'list_forum_post': list_forum_post,
        'all_forums': list_forums,
        'cat_slug': ct_slug,
    }
    return render(request, 'forum/forum.html', data)


def index(request):
    all_disc = Discussion.objects.filter(parent__isnull=True).order_by('-id')
    list_forums = all_forums(request).distinct().order_by("-id")
    page = request.GET.get('page', 1)

    paginator = Paginator(all_disc, 8)
    try:
        all_disc = paginator.page(page)
    except PageNotAnInteger:
        all_disc = paginator.page(1)
    except EmptyPage:
        all_disc = paginator.page(paginator.num_pages)

    data = {
        'posts': all_disc,
        'all_forums': list_forums
    }

    return render(request, 'forum/index.html', data)


def discussion(request, slug):
    disc = get_object_or_404(Discussion, slug=slug, status="published")
    list_forums = all_forums(request)
    if disc is None:
        messages.error(request, 'Topic is not active anymore!')
    else:
        pass

    child = Discussion.objects.filter(parent=disc.id, status="published")

    data = {
        'disc': disc,
        'all_forums': list_forums,
        'child': child,
        'slug': slug
    }

    return render(request, 'forum/discussion.html', data)


def create_disc(request):
    if request.POST.get('action') == 'POST':

        Fid = int(request.POST.get('ForumId'))
        disc = request.POST.get('rp')
        tp = request.POST.get('tp')
        author = request.user.id
        if disc == "" or tp is "":
            # messages.error(request, "Field is required")
            raise disc.ValidationError(request, "Field is required")
            pass

        # Get Instances of Forum and Discussion to use in TRY
        ForumId = get_object_or_404(Forum, pk=Fid)

        response: JsonResponse = JsonResponse({'ForumId': ForumId.pk, 'tp': tp, 'disc': disc})

        if request is None:
            return HttpResponse(status=400)
        else:
            create_insert = Discussion.objects.create(title=tp, discuss=disc, forum=ForumId, author_id=author)
            if create_insert:
                create_insert.save()

            return HttpResponse(response)



def post_reply(request):
    if request.POST.get('action') == 'POST':
        rpId = int(request.POST.get('id'))
        Fid = int(request.POST.get('ForumId'))
        disc = request.POST.get('rp')
        author = request.user.id
        if disc == "":
            # messages.error(request, "Field is required")
            raise disc.ValidationError(request, "Field is required")
            pass

        # Get Instances of Forum and Discussion to use in TRY
        ForumId = get_object_or_404(Forum, pk=Fid)
        rpId = get_object_or_404(Discussion, pk=rpId)

        response: JsonResponse = JsonResponse({'rpId': rpId.pk, 'ForumId': ForumId.pk, 'disc': disc})

        if request is None:
            return HttpResponse(status=400)
        else:
            try:
                parentId = Discussion.objects.get(pk=rpId.pk, author_id=author)
                Discussion.objects.filter(pk=parentId.pk, forum=ForumId.pk, author_id=author).update(discuss=disc)
                print("hello1")
            except ObjectDoesNotExist:
                reply_insert = Discussion.objects.create(parent=rpId, discuss=disc, forum=ForumId, author_id=author)
                print("hello2")
                reply_insert.save()

            return HttpResponse(response)
        # else:
        #     messages.error(request, "You data is not valid")


def reply_reply(request):
    if request.POST.get('action') == 'POST':
        reply_id = int(request.POST.get('reply_id'))
        reply = request.POST.get('reply')
        Fid = int(request.POST.get('forum'))
        author = request.user.id

        if reply == "":
            raise ValidationError("Field is required")
            pass

        # Get Instances of Forum and Discussion to use in TRY
        ForumId = get_object_or_404(Forum, pk=Fid)
        replyId = get_object_or_404(Discussion, pk=reply_id)

        response: JsonResponse = JsonResponse({'replyId': replyId.pk, 'ForumId': ForumId.pk, 'reply': reply})

        print(response)

        if request is None:
            return HttpResponse(status=400)
        else:
            try:
                parentId = Discussion.objects.get(pk=replyId.pk, author_id=author)
                Discussion.objects.filter(pk=parentId.pk, forum=ForumId.pk, author_id=author).update(discuss=reply)
            except ObjectDoesNotExist:
                reply = Discussion.objects.create(parent=replyId, discuss=reply, forum=ForumId, author_id=author)
                reply.save()

            return HttpResponse(response)


def owner_post_delete(request):
    if request.POST.get('action') == 'POST':
        del_id = int(request.POST.get('reply_id'))
        author = request.user.id
        del_post = get_object_or_404(Discussion, pk=del_id, author_id=author)

        response: JsonResponse = JsonResponse({'pk': del_id, 'owner': author})
        if request is None:
            return HttpResponse(status=400)
        else:
            del_post.delete()  # Delete the record
            return HttpResponse(response)


def add_claps(request):
    if request.POST.get('action') == 'POST':
        clap_id = int(request.POST.get('clap_id'))
        get_clap = int(request.POST.get('clap_rep'))
        author = request.user.id
        # count_index = 0
        get_clap += 1
        # Get Instances of Forum and Discussion to use in TRY
        clap_up = get_object_or_404(Discussion, pk=clap_id)

        print(clap_id)
        print(get_clap)

        response: JsonResponse = JsonResponse({'clap_up': clap_up.pk, 'get_clap': get_clap})

        print(response)

        if request is None:
            return HttpResponse(status=400)
        else:
            Discussion.objects.filter(pk=clap_up.pk).update(claps=get_clap)
            return HttpResponse(response)

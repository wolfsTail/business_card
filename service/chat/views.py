from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from chat.models import Group


@login_required
def group_chat(request, uuid):
    context = {}

    group = get_object_or_404(Group, uuid=uuid)
    if request.user not in group.members.all():
        raise Http404
    
    messages = group.messages.order_by("-timestamp")
    events = group.events.order_by("-timestamp")

    messages_events = [*messages, *events]

    group_members = group.members.all()

    context["messages_events"] = messages_events
    context["group_members"] = group_members

    return render(request, "chat/helpchat.html", context=context)

@login_required
def check_incidents(request):
    context = {}

    groups = Group.objects.all()
    user = request.user

    context["groups"] = groups
    context["user"] = user
    
    return render(request, "chat/incidents.html", context=context)

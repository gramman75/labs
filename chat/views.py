
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django_socketio import broadcast, broadcast_channel, NoSocket
from django.template import RequestContext

from chat.models import ChatRoom


def rooms(request, template="chat/rooms.html"):
    """
    Homepage - lists all rooms.
    """
    context = {"rooms": ChatRoom.objects.all()}
    # return render_to_response('common/index.html',context_instance=RequestContext(request))   
    return render(request, template, context)


def room(request, slug, template="chat/room.html"):
    """
    Show a room.
    """
    context = {"room": get_object_or_404(ChatRoom, slug=slug)}
    return render_to_response(template, context, context_instance=RequestContext(request))
    # return render(request, template, context)


def create(request):
    """
    Handles post from the "Add room" form on the homepage, and
    redirects to the new room.
    """
    name = request.POST.get("name")
    if name:
        room, created = ChatRoom.objects.get_or_create(name=name)
        return redirect(room)
    return redirect(rooms)


@user_passes_test(lambda user: user.is_staff)
def system_message(request, template="chat/system_message.html"):
    context = {"rooms": ChatRoom.objects.all()}
    if request.method == "POST":
        room = request.POST["room"]
        data = {"action": "system", "message": request.POST["message"]}
        try:
            if room:
                broadcast_channel(data, channel="room-" + room)
            else:
                broadcast(data)
        except NoSocket, e:
            context["message"] = e
        else:
            context["message"] = "Message sent"
    return render(request, template, context)
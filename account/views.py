from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from .models import Profile, Contact
from actions.utils import create_action
from actions.models import Action


@login_required()
def dashboard(request):
    """
    one complete query is better than multiple queries. so with select_related we can fetch attach related foreignkey
    and one to one fields that related with current actions and with prefetch_related we can fetch and attach many to
    many related with current action. so with one complete query we have all required data such as complete user object
    and user_profiles and complete target object.
    """
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'actions': actions})


def register(request):
    if request.method == 'POST':
        new_user = UserRegisterForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account.', )
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
        return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully!")
            return HttpResponseRedirect('/account/edit/')
        else:
            messages.add_message(request, messages.ERROR, "Profile updating failed!")
            return HttpResponseRedirect('/account/edit/')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})


@ajax_required
@login_required
@require_POST
def user_follow(request):
    user_id = request.POST.get('id')  # this is user id that we are in profile
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Board,Topic,Post      # النقطة دى تشير الى انه فى نفس الفولدر
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm

# Create your views here.

def signup(request):
    # form = UserCreationForm()
    form = SignUpForm()
    if request.method=='POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request,user)   # اعمل دخول ببيانات المستخدم دا
            return redirect('home')


    return render(request,'signup.html',{'form':form})



def validate_Username(request):
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username).exists()
    data = { 'is_taken' : is_taken }    # data in json because we use ajax
    if data['is_taken']:
        data['error_message'] = "The User Already Taken"
    return JsonResponse(data)

# {%block content%}
#     <span id="user_error"></span>
#     <form method="post" data-validate-username-url={%url '/validate_username/'%}>
#         {%csrf_token%}
#         {{form.as_p}}
#         <button type="submit">Sign Up</button>
#     </form>
# {%endblock%}

# {%block javascript%}
# <script>
# $("id_username").change(() => {
#    let username = $(this).val();
#    let form = $(this).closest("form"); 
#    $.ajax({
#       url : form.attr(data-validate-username-url),
#       data : form.serialize(),     # جيب ليا كل البيانات ال اتت مع الفورم
#       dataType:'json',
#       success : function(data){
#       if (data.is_taken){
#               $("#user_error").text(data.error_message)
#       }
#   }
# })
# )}
# </script>
#
# {%endblock%}
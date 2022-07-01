from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,JsonResponse
from .models import Board,Topic,Post      # النقطة دى تشير الى انه فى نفس الفولدر
from django.contrib.auth.models import User
from .forms import NewTopicForm,PostForm
from django.contrib.auth.decorators import login_required
from rest_framework import APIView,serializers
from rest_framework.response import Response
from .Serializers import BoardSerializer , TopicSerializer
from rest_framework import status    
# Create your views here. 

def home(request):
    boards = Board.objects.all()
    # boards_names = []
    # for board in boards:
    #     boards_names.append(board.name)
    # print(boards_names)
    # response_html = '<br>'.join(boards_names)
    # data = {'Results':list(boards.values("pk","name","description"))}
    # return JsonResponse(data)

    return render(request,'home.html',{'boards':boards}) # الريندر الطبيعى بتاعه انه بيدخل فولدر التيمبلت ويدور عن التيمبلت ال انا كتبتها
    # يتم ارسال البيانات الى الصفحة عن طريق الديكشنرى يحتوى على المفتاح والقيمة

def board_topics(request,board_id):
    # try:
    #     board = Board.objects.get(pk = board_id)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board,pk=board_id)
    # topics = board.topics.order_by('-created_dt').annotate(comment=Count('posts'))
    # data = {"results":{
    #     "name":board.name,
    #     "description":board.description
    # }}
    # return JsonResponse(data)
    return render(request,'topic.html',{'board':board})
    # frontend venv
    # def board_list(request):
    #     backend_url="http://127.0.0.1:8000/"
    #     backend_url="http://127.0.0.1:8000/boards/"+str(board_id)+"/"
    #     headers = {'Content_Type':"application/json"}
    #     response = request.get(backend_url,headers=headers)
    #     boards = response.json()
    #     return render(request,'home.html',{'boards':boards['Results'])

# class BoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Board
#         fields = '__all__'

# class TopicSerializer(serializers.ModelSerializer):
#     boards = BoardSerializer(many=True,raed_only=True)
#     board_name = Serializers.CharField(source="board.name",required=False)
#     creater_name = serializers.CharField(source="created_by.username",required=False)
#     class Meta:
#         model = Topic
#         fields = '__all__'        

# class BoardList(APIView):
#     def get(self,request):
#         boards = Board.objects.all()
#         data = BoardSerializer(boards,many=True).data
#         return Response(data)

#     def post(self,request):
#         serializer = BoardSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors,status = status.HTTP_404_BAD_REQUEST)



# class BoardTopics(APIView):
#     def get(self,request,board_id)
#         board = get_object_or_404(Board,pk=board_id)
#         topics = board.topics.order_by('-created_dt').annotate(comment=Count('posts'))
#         data = TopicSerializer(topics,many=True).data      # هذا السطر يغنينا عن الثلاث اسطر ال تحت
#         return Response(data)
#         data = {"results":{
#         "name":board.name,
#         "description":board.description
#     },}


# def BoardDetails(APIView):
#     def get(self,request,board_id):
#         board = get_object_or_404(board,pk=board_id)
#         data = BoardSerializer(board).data
#         return Response(data)

#########################################################################################

@login_required
def new_topic(request,board_id): 
    board = get_object_or_404(Board,pk=board_id)
    form = NewTopicForm()
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid:      # Make Validation
            topic = form.save(commit=False)    # يعنى مش تقوم بعملية الحفظ دلوقت
            topic.board = board
            topic.created_by = request.user
            topic.save()
            post = Post.objects.create(       # هذه الدالة بتعمل حفظ تلقائيا
                message = form.cleaned_data.get('message'),
                created_by = request.user ,    # سجل ليا اسم ال قام بالتسجيل الان وليس اول اسم عندك
                topic = topic
            )
            return redirect ('board_topics',board_id=board.pk)
    else:
        form = NewTopicForm()

    # if request.method == 'POST' :
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     user = User.objects.first()
    #     topic = Topic.objects.create(
    #         subject = subject,
    #         board = board_id,
    #         created_by = user,
    #     )
    #     post = Post.objects.create(
    #         message = message ,
    #         topic = topic,
    #         created_by = user,
    #     )
    #     return redirect('board_topics',board_id=board.pk)

    return render (request,'new_topic.html',{'board':board,'form':form})


def about(request):
    return render(request,'about.html') 


def topic_posts(request,board_id,topic_id):
    # الشرطتين بتجيب جميع العلاقات بين الجداول relation
    topic = get_object_or_404(Topic,board__pk=board_id,pk=topic_id)
    return render(request,'topic_posts.html',{'topic':topic})    

@login_required
def replay_topic(request,board_id,topic_id):
    # الشرطتين بتجيب جميع العلاقات بين الجداول relation
    topic = get_object_or_404(Topic,board__pk=board_id,pk=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            Post = form.save(commit=False)    # يعنى مش تقوم بعملية الحفظ دلوقت
            Post.topic = topic
            Post.created_by = request.user
            Post.save()
            
            return redirect ('topic_posts',board_id=board.id,topic_id=topic_pk)
    else:
        form = PostForm()    
    return render(request,'replay_topic.html',{'topic':topic,'form':form})

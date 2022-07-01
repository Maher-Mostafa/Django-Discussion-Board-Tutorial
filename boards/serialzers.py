from rest_framework import serializers
from .models import *

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TopicSerializer(serialzers.ModelSerialzer):
    class Meta:
        model = Topic
        fields = '__all__'

class PostSerializer(serialzers.ModelSerialzer):
    class Meta:
        model = Post
        fields = '__all__'


class TopicSerializer(serialzers.ModelSerialzer):
    class Meta:
        model = Topic
        fields = '__all__'



from boards.serializers import BoardSerializer
from boards.models import Board
board_serializer = BoardSerializer(data={"name":"test_board","description":"test board serial"})
board_serializer.is_valid()
board_data = board_serializer.save()
board_data.pk
board_serial = board_serializer(instance=board_data, data={'name':"update_board","description":"............."})
board_serial.is_valid()
board_serial.save()
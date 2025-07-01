from .models import Like, Bookmark,Comment
from rest_framework import serializers


#user.username,todo.name

class LikeSerializer():
    username=serializers.CharField(source="user.username",read_only=True)
    todo_name=serializers.CharField(source="todo.name",read_only=True)
    class Meta:
        model =Like
        fields=["id","todo","todo_name","user","username","is_like"]
        read_onlyfields=["user"]
# read_only=True: 이 필드는 출력전용으로 클라이언트가 값을 보내도 
# 저장에는사용되지 않습니다.

class BookmarkSerializer():
    username=serializers.CharField(source="user.username",read_only=True)
    class Meta:
        model =Bookmark
        fields=["id","todo","todo_name","user","username","is_marked"]
        read_onlyfields=["user"]

class CommentSerializer():
    username=serializers.CharField(source="user.username",read_only=True)
    todo_name=serializers.CharField(source="todo.name",read_only=True)

    like_count = serializers.SerializerMethodField()
    class Meta:
        model =Comment
        fields=["id","todo","todo_name","user","username","content"
                ,"created_at","like_count"]
        read_onlyfields=["todo","user","created_at"]
        # 폼에서 사용자가 수정할 수 없어야 하는 필드를 명확히 구분해주기 위한 용도

    def get_like_count(self,obj):
        return obj.likes.count()

    def get_is_liked(self,obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False



class CommentLikeSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source="user.username",read_only=True)
    comment_content= serializers.CharField(source="comment.content",read_only=True)

    class Meta:
        model =Comment
        fields=["id","user","username","comment","comment_contetnt","is_like"]
        read_onlyfields=["todo","user","created_at"]
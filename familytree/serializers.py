from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from familytree.models import *


class MyParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ["first_name", "last_name", "parent_relation"]


class MySiblingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sibling
        fields = ["first_name", "last_name", "sibling_relation"]


class MyChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ["first_name", "last_name", "children_relation"]


class MyUserSerializer(serializers.ModelSerializer):
    parant_user = MyParentsSerializer(many=True, read_only=True)
    siblings_user = MySiblingSerializer(many=True, read_only=True)
    children_user = MyChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = MyUser
        fields = ["first_name", "last_name", "email", "gender",
                  "parant_user", "siblings_user", 'children_user']


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message',)


class CommentSerializer(serializers.ModelSerializer):
    subcomment = SubCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('sub_chat', 'message', 'subcomment',)

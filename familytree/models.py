from email import message
from django.db import models
from familytree.choice import *
# Create your models here.


class CommanTime(models.Model):
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True)

    class Meta:
        abstract = True
    

class MyUser(CommanTime):
    first_name = models.CharField("First Name", blank=True, null=True, max_length=255)
    last_name = models.CharField("Last Name",blank=True,null=True,max_length=255)
    email = models.EmailField("Email",unique=True,max_length=255)
    gender = models.CharField("Gender",choices=GENDER, default="Male", max_length=20)
    def __str__(self):
        return self.first_name +" " +self.last_name
    class Meta:
        verbose_name_plural = "My User"

class Parents(CommanTime):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="parant_user",blank=True,null=True)
    first_name = models.CharField("First Name", blank=True, null=True, max_length=255)
    last_name = models.CharField("Last Name",blank=True,null=True,max_length=255)
    parent_relation = models.CharField("Parent Relation",choices=PRAENT_RELATION, default="Father", max_length=20)
    def __str__(self):
        return self.first_name +" " +self.last_name
    class Meta:
        verbose_name_plural = "Parents"


class Sibling(CommanTime):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="siblings_user",blank=True,null=True)
    first_name = models.CharField("First Name", blank=True, null=True, max_length=255)
    last_name = models.CharField("Last Name",blank=True,null=True,max_length=255)
    sibling_relation = models.CharField("Sibling Relation",choices=SIBLING_RELATION, default="Brother", max_length=20)
    def __str__(self):
        return self.first_name +" " +self.last_name
    class Meta:
        verbose_name_plural = "Siblings"


class Children(CommanTime):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name="children_user",blank=True,null=True)
    first_name = models.CharField("First Name", blank=True, null=True, max_length=255)
    last_name = models.CharField("Last Name",blank=True,null=True,max_length=255)
    children_relation = models.CharField("Children Relation",choices=CHILDREN_RELATION, default="Son", max_length=20)
    def __str__(self):
        return self.first_name +" " +self.last_name
    class Meta:
        verbose_name_plural = "Children"


class Comment(CommanTime):
    sub_chat = models.ForeignKey('self', blank=True, on_delete=models.CASCADE,null=True, related_name='subcomment')
    message = models.TextField()

    def __str__(self):
        return str(self.id)
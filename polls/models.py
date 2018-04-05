from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User_Register(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50,null=True,blank=True)
    payment = models.CharField(max_length=50)



class IMG(models.Model):
    img = models.ImageField(upload_to='img')

    name = models.CharField(max_length=20)
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default='M')


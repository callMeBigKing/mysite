from django.contrib import admin

from .models import Question,Choice,User_Register,IMG

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User_Register)
admin.site.register(IMG)

from django.contrib import admin
from .models import contact, Profile, Primary, Secondary, Tetiary, Skill_1, Skill_2, Skill_3, Interest, Experience
# Register your models here.

admin.site.register(Profile)
admin.site.register(Primary)
admin.site.register(Secondary)
admin.site.register(Tetiary)
admin.site.register(Skill_1)
admin.site.register(Skill_2)
admin.site.register(Skill_3)
admin.site.register(Interest)
admin.site.register(Experience)
admin.site.register(contact)
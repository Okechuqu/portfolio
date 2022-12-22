from django.db import models


class Profile(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Primary(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Secondary(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tetiary(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skill_1(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Skill_2(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Skill_3(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Interest(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

from django.db import models

# declare a new model with a name "GeeksModel"
class Message(models.Model):
    # fields of the model
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, default="")
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


class Curriculum(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name

from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/%Y/%m/%d', null=True)

    def __str__(self):
        return self.subject

class Lesson(BaseModel):
    subject = models.CharField(max_length=100)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lessons/%Y/%m/%d', null=True)

    class Meta:
        unique_together = ('subject', 'course')

    def __str__(self):
        return self.subject

class Comment(BaseModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.lesson}"

class Rating(BaseModel):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating by {self.user} on {self.lesson}"

class Tag(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class LessonTags(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesson} - {self.tag}"
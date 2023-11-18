from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.project.title} -> {self.user.get_username()}"


class Cart(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} >>> {self.cart.title}"

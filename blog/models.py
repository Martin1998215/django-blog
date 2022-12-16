from django.db import models


class Mypost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    my_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-my_date"]


class Comment(models.Model):
    post = models.ForeignKey(
        Mypost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    my_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-my_date"]


# class Customer(models.Model):

#     name = models.CharField(max_length=255)
#     email = models.EmailField()


# class Custom(models.Model):

#     name = models.CharField(max_length=255)
#     email = models.EmailField()

#     def __str__(self):

#         return self.name

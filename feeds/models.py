from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("post_user"))
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Posted by {self.user} at {self.created_at}"
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("like_user"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name=("like_post"))
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("user", "post") # Prevent duplicate likes عشان المستخدك ميعملش لايك علي نفس البوست اكتر من مره
    def str (self):
        return f"{self.user} liked post {self.post.id}"
    



class Comment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("comment_user"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name=("comment_post"))
    comment = models.TextField()
    likes = models.ManyToManyField(User, related_name="comments_liks", blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def str (self):
        return f"Comment by {self.user.username} on post {self.post.id}"


class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reposts_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reposts_post")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str (self):
         return f"{self.user.username} reposted post {self.post.id}"
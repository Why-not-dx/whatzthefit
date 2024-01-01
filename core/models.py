from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    NEW = "New"
    SEEN = "Seen"
    TODO = "Todo"
    RES = "Res" 
    STATUS_CHOICES = [
        (NEW, "New message"),
        (SEEN, "Read and no action required"),
        (TODO, "Actions are to be performed"),
        (RES, "issues resolved"),
    ]

    user = models.ForeignKey(User, related_name="user_message", on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    content = models.TextField()
    msg_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=NEW)


    class Meta:
        ordering = ("msg_date", "user")
        verbose_name_plural = "Messages" # to user the correct word in admin page instead of the table name
    
    def __str__(self):
        # To show of the name of the object instead of the ID in amdin page
        return self.topic


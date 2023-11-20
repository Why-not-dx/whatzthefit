from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories" # to user the correct word in admin page instead of the table name
    
    def __str__(self):
        # To show of the name of the object instead of the ID in amdin page
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Brands" # to user the correct word in admin page instead of the table name
    
    def __str__(self):
        # To show of the name of the object instead of the ID in amdin page
        return self.name


class Body(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Bodies"
    

class Item(models.Model):
    name = models.CharField(max_length=300)
    details = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="user_items", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="category_items", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name = "items", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="items_images", blank=True, null=True)
    body = models.ForeignKey(Body, related_name="body_items", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name 



class Posts(models.Model):
    poster = models.ForeignKey(User, related_name="poster_posts", on_delete=models.CASCADE)
    fit_grade = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    item = models.ForeignKey(Item, related_name="item_posts", on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('post_date', "item")
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return f"{self.poster.username} - {self.item.name}"

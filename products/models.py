from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Products(models.Model):
    company = models.ForeignKey("auth.User", verbose_name=("Satıcı şirkət"), on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, verbose_name="Məhsulun adı")
    price = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name="Məhsulun dəyəri")
    quality = RichTextUploadingField(verbose_name="Məhsulun keyfiyyəti")
    country = models.CharField(max_length=100 , verbose_name="İxrac ölkəsi")
    end_date = models.DateField(auto_now_add=True)
    # image = models.FileField(upload_to="Product Images",blank=True, null=True,verbose_name="Şəkil")

    
    def __str__(self) :
        return f"{self.company} => {self.name}"
    
    
class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name=" Məhsul", related_name = "comments")
    comment_author = models.CharField(max_length=100, verbose_name = "Müştəri")
    comment_content =models.TextField(verbose_name="Rəy")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.comment_author} - {self.comment_content}"
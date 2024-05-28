from django.db import models

# Create your models here.
class Products(models.Model):
    company = models.ForeignKey("auth.User", verbose_name=("Satıcı şirkət"), on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, verbose_name="Məhsulun adı")
    price = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name="Məhsulun dəyəri")
    quality = models.TextField(max_length=150,verbose_name="Məhsulun keyfiyyəti")
    country = models.CharField(max_length=100 , verbose_name="İxrac ölkəsi")
    end_date = models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return f"{self.company} => {self.name}"
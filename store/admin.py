from django.contrib import admin
from .models import About, Categorie, Comment, Contact, FaQs ,Product
# Register your models here.


admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Comment)

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(FaQs)
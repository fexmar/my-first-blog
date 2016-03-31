
# Register your models here.

from django.contrib import admin
from .models import Post

#Nombre: djangogirls/blog/admin.py

#Registra nuestro objeto post en el administador
#de Django para poder consultar o actualiza informacion del post.

admin.site.register(Post)

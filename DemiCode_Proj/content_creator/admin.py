from django.contrib import admin
from .models import Image, Bank, Blog, Digital_Product, Video, Review, Code_Snippet

# Register your models here.
admin.site.register(Bank)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(Digital_Product)
admin.site.register(Video)
admin.site.register(Review)
admin.site.register(Code_Snippet)


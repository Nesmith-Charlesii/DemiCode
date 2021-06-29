from django.db import models


# Create your models here.
class Creative(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    # confirmPW = models.CharField(max_length=150)
    debit_card = models.BigIntegerField(null=True, blank=True)
    photo_upload = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Content Creator: {self.first_name} {self.last_name}'


class Blog(models.Model):
    title = models.CharField(max_length=50)
    # TextField increases in size. Does not need a max limit
    content = models.TextField()
    header_image = models.ImageField(upload_to='images/', null=True)
    creator = models.ForeignKey(Creative, related_name="articles", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Blog: {self.title}'


class Digital_Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    price = models.FloatField()
    seller = models.ForeignKey(Creative, related_name="products", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Product: {self.name}'


class Review(models.Model):
    comment = models.CharField(max_length=100)
    anon_name = models.CharField(max_length=50, null=True, blank=True)
    # ManyToManyField represented with an empty array in JSON
    Thumbs_Upped = models.ManyToManyField(Creative, related_name="likes", null=True, blank=True)
    Likes = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(Creative, related_name="comments", null=True, blank=True, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.comment}'


class Code_Snippet(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    upload = models.ImageField(upload_to='images/', null=True)
    creator = models.ForeignKey(Creative, related_name="snippets", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Snippet: {self.title}'


class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/')
    creator = models.ForeignKey(Creative, related_name="videos", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Video: {self.title}'

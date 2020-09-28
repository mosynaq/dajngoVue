from django.db import models


class Author(models.Model):
    id = models.AutoField("ID", primary_key=True)
    first_name = models.CharField("First Name", max_length=100, null=False)
    last_name = models.CharField("Last Name", max_length=100, null=False)
    date_of_birth = models.DateField("Date of Birth")
    bio = models.TextField("Biography", null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class WorkOfArt(models.Model):
    id = models.AutoField("ID", primary_key=True)
    title = models.CharField("Title", max_length=1000)

    class WorkOfArtTypes(models.TextChoices):
        book = "book", "Book"
        article = "article", "Article"

    type = models.CharField(choices=WorkOfArtTypes.choices, max_length=20, default=WorkOfArtTypes.book, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="works_of_art", null=False)
    description = models.TextField("Description", blank=True, null=True)
    rating = models.PositiveSmallIntegerField("Rating", default=0)
    image = models.URLField("Image URl", null=True)
    price = models.DecimalField("Price", max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.title}, a {self.type} by {self.author}"

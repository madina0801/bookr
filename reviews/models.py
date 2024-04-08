from django.db import models
from django.contrib import auth


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField("Contributor", through="BookContributor")


class Contributor(models.Model):
    firstName = models.CharField(
        max_length=50, help_text="The contributor's first name or names"
    )
    lastName = models.CharField(
        max_length=50, help_text="The contributor's last name or  names"
    )
    email = models.EmailField(help_text="The contact email for the contributor")


class Review(models.Model):
    content = models.TextField(help_text="The Review text")
    rating = models.IntegerField(help_text="The Rating the reviewr has given")
    models.DateTimeField(
        auto_now_add=True, help_text="The date and time the review was created."
    )
    date_edited = models.DateTimeField(
        null=True, help_text="The date and time the review was last edited."
    )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, help_text="The Book that this review is for."
    )

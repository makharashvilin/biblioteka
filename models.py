from django.db import models



class Library(models.Model):
    name = models.CharField(max_length=100)



class LibraryCard(models.Model):
    card_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=200)

# screenshi pirveli card1 da card2 arasworad shevkmeni da washla damaviwkda;*

class Member(models.Model):
    name = models.CharField(max_length=50)
    joined_date = models.DateField()
    library_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE, related_name='member')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='members')
    books = models.ManyToManyField(Book, related_name='members')


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # other fields...

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]

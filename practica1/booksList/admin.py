from django.contrib import admin

import models

admin.site.register(models.Books)
admin.site.register(models.Author)
admin.site.register(models.Genere)
admin.site.register(models.BooksReview)
admin.site.register(models.AuthorReview)

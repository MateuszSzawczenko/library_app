from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from .models import *
from .forms import *
from django.db.models.query import EmptyQuerySet
from .filters import BookFilter
import requests

from .common.util.google_books_api import *

# Create your views here.


def home(response):
    return render(response, 'main/home.html', {})


def create_new_records_in_db(response):

    ls = ListOfBooks.objects.get(id=1)

    if response.method == "POST":

        if response.POST.get("newItem"):

            ttl = response.POST.get("newTittle")
            author = response.POST.get("newAuthor")
            date_pub = response.POST.get("newDate")
            isbn = response.POST.get("newIsbn")
            pages_no = response.POST.get("newPagesNo")
            link = response.POST.get("newLink")
            lang = response.POST.get("newLanguage")

            ls.book_set.create(title=ttl, author=author, date_published=date_pub, isbn_number=isbn,
                                                 pages_number=pages_no, page_title_href=link, language_published=lang)

        elif response.POST.get("clearList"):
            for item in ls.book_set.all():

                item.delete()

        for item in ls.book_set.all():
            if response.POST.get("editItem" + str(item.id)):
                item.edit_status = True
                item.save()

            elif response.POST.get("submitItemChanges" + str(item.id)):
                new_ttl = response.POST.get("editTitle" + str(item.id))
                item.title = new_ttl
                item.edit_status = False
                item.save()
    return render(response, 'main/create.html', {"ls": ls})


def view_all_books(response):

    ls = ListOfBooks.objects.get(id=1)

    books = ls.book_set.all()

    my_filter = BookFilter(response.GET, queryset=books)
    books = my_filter.qs


    return render(response, 'main/books.html', {"ls": ls, "books": books, "myFilter": my_filter})


def import_books_from_google_api(response):

    ls = ListOfBooks.objects.get(id=1)

    if response.method == "POST":

        if response.POST.get("importBooks"):

            key_word = response.POST.get("keyWord")

            books_from_api_json = get_books_from_google_api_filter_with_provided_key_word({"q": key_word})

            books_titles, books_authors, books_publication_dates, books_isbn, books_page_count, books_image_links, books_languages = get_books_info_final_forms_from_raws_gathered_form_json(books_from_api_json)

            for title, author, date, isbn, count, link, lang in zip(books_titles, books_authors, books_publication_dates, books_isbn, books_page_count, books_image_links, books_languages):

                try:
                    ttl = title
                except IndexError:
                    ttl = ''
                try:
                    auth = author[0]
                except IndexError:
                    auth = ''
                try:
                    date = str(date)[0:4]
                    date_pub = int(date)
                except ValueError or IndexError:
                    date_pub = 0

                try:
                    isbn_ = isbn[0]["type"]
                except IndexError:
                    isbn_ = ''

                try:
                    if type(count) == str:
                        pages_no = 0
                    else:
                        pages_no = count
                except IndexError:
                    pages_no = 0

                try:
                    img_link = link["thumbnail"]
                except IndexError:
                    img_link = ''

                try:
                    pub_lang = lang
                except IndexError:
                    pub_lang = ''

                ls.book_set.create(title=ttl, author=auth, date_published=date_pub, isbn_number=isbn_,
                                   pages_number=pages_no, page_title_href=img_link, language_published=pub_lang)

            '''for title, author, date, isbn, page_count, image_link, language in books_titles, books_authors, books_publication_dates, books_isbn, books_page_count, books_image_links, books_languages:
                print(title, author, date, isbn, page_count, image_link, language)'''

            #print(books_titles)

    return render(response, 'main/google_api.html', {})



'''        elif response.POST.get("clearList"):
            for item in ls.product_set.all():
                item.delete()'''

'''for item in ls.product_set.all():
    if item.text == txt:
        item.amount += amount
'''
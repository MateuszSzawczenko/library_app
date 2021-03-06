import requests
import json


def get_books_from_google_api_filter_with_provided_key_word(params):

    URL = "https://www.googleapis.com/books/v1/volumes"
    r = requests.get(url=URL, params=params)
    data = r.text
    data_json = json.loads(data)

    return data_json


def get_books_info_from_json_response(data_json, info_type):
    books_info = []
    for item in data_json["items"]:

        try:
            books_info.append(item["volumeInfo"][info_type])
        except KeyError:
            books_info.append("")

    return books_info


def get_books_info_final_forms_from_raws_gathered_form_json(books_from_api_json):

    books_titles = get_books_info_from_json_response(books_from_api_json, "title")
    books_authors = get_books_info_from_json_response(books_from_api_json, "authors")
    books_publication_dates = get_books_info_from_json_response(books_from_api_json, "publishedDate")
    books_isbn = get_books_info_from_json_response(books_from_api_json, "industryIdentifiers")
    books_page_count = get_books_info_from_json_response(books_from_api_json, "pageCount")
    books_image_links = get_books_info_from_json_response(books_from_api_json, "imageLinks")
    books_languages = get_books_info_from_json_response(books_from_api_json, "language")

    return books_titles, books_authors, books_publication_dates, books_isbn, books_page_count, books_image_links, books_languages

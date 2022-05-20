from django.urls import path

from online_library.web.views import show_home, add_book, edit_book, book_details, show_profile, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = (
    path('', show_home, name='show home'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>', delete_book, name='book delete'),

    path('profile/', show_profile, name='profile'),
    path('create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)

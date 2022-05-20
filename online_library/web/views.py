from django.shortcuts import render, redirect

from online_library.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, AddBookForm, EditBookForm
from online_library.web.models import Profile, Book


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    books_3 = [books[x:x+3] for x in range(0, len(books), 3)]
    context = {
        'books': books,
        'profile': profile,
        'books_3': books_3
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = AddBookForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        'profile': profile,
        'book': book,
    }

    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):

    Book.objects.filter(pk=pk).delete()

    return redirect('show home')


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)



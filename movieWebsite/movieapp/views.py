from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.utils.text import slugify

from .models import Movie, Category, UserMovie, User,Review
from .forms import MovieForm, ReviewForm


# Create your views here.



def movie_list(request, c_slug=None):
    complete_movie = Movie.objects.all()
    user_movie_list = UserMovie.objects.all()
    c_page = None
    products = None
    if c_slug != None:
        # c_page = get_object_or_404(Category, slug=c_slug)
        c_page = Category.objects.get(slug=c_slug)
        movies = UserMovie.objects.all().filter(category=c_page)
    else:
        movies = UserMovie.objects.all()
    return render(request, 'movie.html', {'category': c_page, 'movies': movies, 'complete_movie': complete_movie,
                                          'user_movie_lists':user_movie_list})


def user_movie(request,m_user=None):

    if request.method == 'POST':
        print(request.POST)
        m_page=None
        if m_user!=None:
            try:
                m_page = get_object_or_404(User, id=m_user)
            except Exception as e:
                raise e
        user = request.POST.get('m_page')
        name = request.POST['name']
        desc = request.POST['desc']
        actor = request.POST['actor']
        link = request.POST['link']
        date = request.POST['date']
        img = request.FILES['img']
        category = request.POST['category']
        m_category=Category.objects.get(id=category)
        m_slug = slugify(name)
        user_movie_list = UserMovie(title=name, description=desc, actors=actor, youtube_link=link, date=date, image=img,
                                    category=m_category,user=user,slug=m_slug)
        user_movie_list.user = request.user
        user_movie_list.save()
        print("user-------------------------------------->",user_movie_list)
        return redirect('/')
    return render(request, "add_movie.html")

def user_movie_list(request,m_user=None):
    m_page=None
    user_movie_list=None
    if m_user!=None:
        try:
            m_page = get_object_or_404(User,id=m_user)
            user_movie_list = UserMovie.objects.all().filter(user=m_page)
        except Exception as e:
            raise e
    return render(request,"usermovie_list.html",{'user_movie_list':user_movie_list,'m_page':m_page})

# testing
# def user_movie_list(request,m_user=None):
#     user_movie_list = UserMovie.objects.all().filter()
#
#     return render(request,"usermovie_list.html",{'user_movie_list':user_movie_list})




# def movieDetail(request,c_slug,m_slug):
#     try:
#         movie=UserMovie.objects.get(category__slug=c_slug,slug=m_slug)
#     except Exception as e:
#         raise e
#     return render(request,"movie-detail.html",{'movieDet':movie})

def movieDelete(request,id):
    movie=UserMovie.objects.get(id=id)
    movie.delete()
    return redirect('/')

def movieEdit(request,id):
    movie=UserMovie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('movieapp:detail', args=[movie.id]))
    return render(request,"movie-edit.html",{'form':form,'movieEdit':movie})

def detail(request,movie_id):
    movie = UserMovie.objects.get(id=movie_id)
    review = Review.objects.filter(movie=movie_id).order_by("-comment")
    return render(request, "movie-detail.html", {'movieDet': movie,'reviews':review})



def add_review(request,id):
    if request.user.is_authenticated:
        movie = UserMovie.objects.get(id=id)
        if request.method == 'POST':
            form=ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                data.movie = movie
                data.save()
                return HttpResponseRedirect(reverse('movieapp:detail',args=[movie.id]))
        else:
            form=ReviewForm()
        return render(request,"detail.html",{'form':form})
    else:
        return redirect('credentials:login')


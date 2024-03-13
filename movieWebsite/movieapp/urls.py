from django.urls import path

from movieapp import views

app_name = 'movieapp'

urlpatterns = [

    path('', views.movie_list, name='movie_list'),
    path('<slug:c_slug>/', views.movie_list, name='movie_list'),
    path('<slug:c_slug>/', views.movie_list, name='movie_by_category'),
    path('user_movie/<m_user>/', views.user_movie, name='user_movie'),
    path('user_movie_list/<m_user>/', views.user_movie_list, name='user_movie_list'),
    # path('<slug:c_slug>/<slug:m_slug>/',views.movieDetail,name='movieDetail'),
    path('movie-delete/<int:id>/',views.movieDelete,name='movieDelete'),
    path('movie-edit/<int:id>/',views.movieEdit,name='movieEdit'),
    path('detail/<int:movie_id>/',views.detail,name='detail'),
    path('addreview/<int:id>/',views.add_review,name='add_review')

]
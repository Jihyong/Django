from django.urls    import path , include
from staticApp        import views

urlpatterns = [
    # http://127.0.0.1:8000/chart/index
    path('index/',  views.index ,    name='static_index'),
    path('line/',   views.line ,     name='static_line'),
    path('bar/',    views.bar ,      name='static_bar'),
]






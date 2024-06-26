'''
views.py - это файл, который содержит все представления Django.

FBV - это функции представления Django.
CBV - это классы представления Django.

objects - это менеджер модели Django, 
который позволяет выполнять запросы к базе данных.

# all() - метод QuerySet, который возвращает все объекты модели.
posts = Post.objects.all() # Получаем QuerySet всех объектов модели Post.
# filter() - метод QuerySet, который возвращает объекты модели, удовлетворяющие условию.
# posts = Post.objects.filter(title__icontains='python')  # Получаем QuerySet объектов модели Post, у которых в поле title содержится 'python'
# exclude() - метод QuerySet, который исключает объекты модели, удовлетворяющие условию.
# posts = Post.objects.exclude(title__icontains='python')  # Получаем QuerySet объектов модели Post, у которых в поле title не содержится 'python'
# order_by() - метод QuerySet, который сортирует объекты модели по указанному полю.
# posts = Post.objects.order_by('created_at')  # Получаем QuerySet объектов модели Post, отсортированных по полю created_at
# reverse() - метод QuerySet, который меняет порядок объектов на обратный.
# posts = Post.objects.reverse()  # Получаем QuerySet объектов модели Post в обратном порядке
# first() - метод QuerySet, который возвращает первый объект модели.
# post = Post.objects.first()  # Получаем первый объект модели Post
# last() - метод QuerySet, который возвращает последний объект модели.
# post = Post.objects.last()  # Получаем последний объект модели Post
# count() - метод QuerySet, который возвращает количество объектов модели.
# count = Post.objects.count()  # Получаем количество объектов модели Post
# exists() - метод QuerySet, который возвращает True, если объекты модели существуют, иначе False.
# exists = Post.objects.exists()  # Проверяем, существуют ли объекты модели Post
# values() - метод QuerySet, который возвращает QuerySet значений указанных полей модели.
# values = Post.objects.values('title', 'created_at')  # Получаем QuerySet значений полей title и created_at модели Post
# values_list() - метод QuerySet, который возвращает QuerySet значений указанных полей модели в виде кортежей.
# values_list = Post.objects.values_list('title', 'created_at')  # Получаем QuerySet значений полей title и created_at модели Post.
# create() - метод QuerySet, который создает новый объект модели.
# post = Post.objects.create(title='New Post', text='New Text')  # Создаем новый объект модели Post
# get() - метод QuerySet, который возвращает один объект модели, удовлетворяющий условию.
# post = Post.objects.get(id=1)  # Получаем объект модели Post с id=1
# update() - метод QuerySet, который обновляет объекты модели, удовлетворяющие условию.
# Post.objects.filter(title__icontains='python').update(title='New Title')  # Обновляем объекты модели Post, у которых в поле title содержится 'python'
# delete() - метод QuerySet, который удаляет объекты модели, удовлетворяющие условию.
# Post.objects.filter(title__icontains='python').delete()  # Удаляем объекты модели Post, у которых в поле title содержится 'python'
Документация Django: https://docs.djangoproject.com/en/4.0/topics/db/queries/

Field lookups - это специальные методы для фильтрации QuerySet по значениям полей модели.
Field lookups:
1. exact - точное совпадение.
2. iexact - точное совпадение без учета регистра.
3. contains - содержит.
4. icontains - содержит без учета регистра.
5. in - входит в список.
6. gt - больше.
7. gte - больше или равно.
8. lt - меньше.
9. lte - меньше или равно.
10. startswith - начинается с.
11. istartswith - начинается с без учета регистра.
12. endswith - заканчивается на.
13. iendswith - заканчивается на без учета регистра.
14. range - в диапазоне.
15. year - год.
16. month - месяц.
17. day - день.
18. week_day - день недели.
19. isnull - равно NULL.
20. regex - регулярное выражение.
21. iregex - регулярное выражение без учета регистра.
Документация: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

Qurey Parameters - это параметры запроса, которые передаются в URL-адресе.
https://exaple.com?name=Esen&age=18&city=Almaty

Paggination:

        # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]
        # limit = 3, page = 1

        # Formula:
        # start = (page - 1) * limit
        # end = page * limit

        # Example 1:
        # page = 1, limit = 3
        # start = (1 - 1) * 3 = 0
        # end = 1 * 3 = 3
        # posts = posts[0:3]

        # Example 2:
        # page = 3, limit = 3
        # start = (3 - 1) * 3 = 6
        # end = 3 * 3 = 9
        # posts = posts[6:9]
'''

from typing import Any
from django.forms.models import BaseModelForm
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from post.models import Post
from post.forms import PostForm, PostForm2, SearchForm


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, World!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


def main_view(request):
   mock_data = [
       {
                'id': 1,
                'title': "I'm blue da ba dee da ba daa",
                'description': "Мем про синего человека",
                'created_at': "2022-01-01",
        },
        {
            'id': 2,
            'title': "Doge",
            'description': "Мем про собаку",
            'created_at': "2022-01-02",
        },
        {
            'id': 3,
            'title': "Pepe the Frog",
            'description': "Мем про лягушку",
            'created_at': "2022-01-03",
        }
    ]
   
   if request.method == 'GET':
       return render(request, 'main.html', {'mock_data': mock_data})


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html' # default: <app_label>/<model_name>_list.html
    context_object_name = 'posts' # default: object_list
    # {'posts': posts}

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs) # {'posts': posts}
        context['name'] = "Esen"
        return context
    
    def get_queryset(self):
        posts = Post.objects.all()  # .exclude(image='')

        return posts


def post_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search') # None
        tags = request.GET.getlist('tags') # [id`1, id`2, id`3]
        ordering = request.GET.get('ordering') # 'title'
        page = int(request.GET.get('page', 1)) # 1

        search_form = SearchForm(request.GET)
        posts = Post.objects.all().select_related('author').prefetch_related('tags')
        # SELECT * FROM post_post JOIN auth_user ON post_post.author_id = auth_user.id

        if search:
            # posts = posts.filter(title__icontains=search) | posts.filter(text__icontains=search)
            posts = posts.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
                )
        if tags:
            # Если тэги постов содержат хотя бы один из выбранных ID
            posts = posts.filter(tags__id__in=tags).distinct()

        if ordering:
            posts = posts.order_by(ordering)

        limit = 4
        max_pages = posts.count() / limit
        # max_pages = 16 / 5 = 3.2
        # round(3.2) = 3 < 3.2 = 3 + 1 = 4
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        posts = posts[start:end]

        context = {'posts': posts, 'name': "Esen", 'search_form': search_form, 'max_pages': range(1, max_pages + 1)}

        return render(request, 'post/post_list.html', context)
    

class PostDetailView(DetailView):
    model = Post
    # template_name = 'post/post_detail.html' # default: <app_label>/<model_name>_detail.html
    context_object_name = 'post' # default: object
    pk_url_kwarg = 'post_id' # default: pk

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['name'] = "Esen"
        return context


def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id) # Получаем объект модели Post по id
        except Post.DoesNotExist:
            return HttpResponse('Post not found', status=404)

        context = {'post': post} 

        return render(request, 'post/post_detail.html', context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm2
    template_name = 'post/post_create.html' # default: <app_label>/<model_name>_form.html
    success_url = '/posts/'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_view')
        form = self.get_form()
        return self.render_to_response({'form': form})

    def form_valid(self, form: BaseModelForm) -> Any:
        form.instance.author = self.request.user
        self.object = form.save()
        return redirect(self.get_success_url())


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post/post_create.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            Post.objects.create_post(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                image=form.cleaned_data['image'],
                # author=request.user
            )

            return redirect('post_list_view')

        return render(request, 'post/post_create.html', {'form': form})
        

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm2
    template_name = 'post/post_update.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    success_url = '/posts/'


def post_update_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse('Post not found', status=404)

    if request.method == 'GET':
        form = PostForm2(instance=post)

        context = {'form': form}

        return render(request, 'post/post_update.html', context)
    
    elif request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect(f'/posts/{post_id}/')

        return render(request, 'post/post_update.html', {'form': form})



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

'''

from django.shortcuts import render, HttpResponse, redirect

from post.models import Post
from post.forms import PostForm, PostForm2


def hello_view(request):
    if request.method == 'GET':
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

    
def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {'posts': posts}

        return render(request, 'post/post_list.html', context)
    

def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id) # Получаем объект модели Post по id
        except Post.DoesNotExist:
            return HttpResponse('Post not found', status=404)

        context = {'post': post} 

        return render(request, 'post/post_detail.html', context)


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post/post_create.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('post_list_view')

        return render(request, 'post/post_create.html', {'form': form})
        
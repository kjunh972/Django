from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(request, 'posts/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post" : post}
    return render(request, 'posts/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        new_post = post_form.save()
        
        
        new_post.save()
        return redirect('post-detail',post_id=new_post.id) #유저가 요청한 제목과 내용을 저장하고 새로운 post.id로 redirect사용해서 
                                                           #post-detail페이지로 이동한다.
    else: #post방식이 아닌 get방식으로 요청할때
        post_form = PostForm() #posts/new 첨으로 이동할때 form을 요청할때.
        return render(request, 'posts/post_form.html', {'form': post_form})
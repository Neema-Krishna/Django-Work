from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
 
from .models import Post,Comments

from .forms import CommentForm


from django.views import View

 
class Starting_page(View):
    def get(self,request):
        latest_post= Post.objects.all().order_by('-date')[:3]
        return render(request,'blog/index.html',{'posts1':latest_post})
    
class Posts(View):
    def get(self,request):
        all_posts=Post.objects.all().order_by("-date")
        return render(request,'blog/alllposts.html',{'allposts':all_posts})

class Post_detail(View):
    def get(self,request,slug):
        form=CommentForm()
        # result=get_object_or_404(Post,slug=slug)
        result=Post.objects.get(slug=slug)
        comments=Comments.objects.filter(post=result).order_by('-id')
        return render(request,'blog/postdetail.html',{'postdetail':result,'form':form, 'comments':comments})
    
    def post(self,request,slug):
        form=CommentForm(request.POST)
        result=Post.objects.get(slug=slug)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=result
            comment.save()
            return HttpResponseRedirect(reverse("post_detail" ,args=[slug]))
        
        form=CommentForm()
        result=Post.objects.get(slug=slug)
        comments=result.comments.all()
        # related name is set as comment else comment_set is to used)
         
        return render(request,'blog/postdetail.html',{'postdetail':result,'form':form,'comments':comments})
    
class ReadLaterView(View):

    def get (self,request):
        stored_posts=request.session.get('stored_posts')
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context['has_posts']=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            context['posts']=posts
            context['has_posts']=True
        return render(request,'blog/stored-posts.html',context)


    def post(self,request):
        stored_posts=request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts=[]
        post_id=int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts']=stored_posts
        
        return HttpResponseRedirect('/')

         

 
        
        

        


  
 


 

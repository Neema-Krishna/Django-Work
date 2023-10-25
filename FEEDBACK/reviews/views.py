from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class ReviewView(View):
     
     def get(self,request):
         
         form=ReviewForm()
         return render(request,"reviews/reviews.html",{'form':form})
     
     def post(self,request):
         form=ReviewForm(request.POST)
         if form.is_valid:
              form.save()
              return HttpResponseRedirect('/thank_you')
         else:
             form=ReviewForm()
             
         return render(request,"reviews/reviews.html",{'form':form})


class ThankyouView(TemplateView):
    #  def get(self,request):
    #     return render(request,'reviews/thankyou.html')
    template_name='reviews/thankyou.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'This works'
        return context
    
# class ReviewView(TemplateView):
#     template_name='reviews/reviewlist.html'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context['reviews']=reviews
#         return context

class ReviewView1(View):
    def get(self,request):
        reviews=Review.objects.all()
        return render(request,'reviews/reviewlist.html',{'reviews':reviews})
 
class SingleReviewView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get('id')
        selected_review=Review.objects.get(pk=id)
        # fav_id=request.session['favourite_review']
        return render(request,'reviews/singlereview.html',
                      {'selected_review':selected_review})
     
    
# class Favorite(View):
#     def post(self,request):
#         review_id=request.POST['review_id']
#         # fav_review=Review.objects.get(pk=review_id)
#         request.session['favourite_review']=review_id
#         return HttpResponseRedirect('/reviews/'+ review_id)



        
    


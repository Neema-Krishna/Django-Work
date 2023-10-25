from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challanges={"january":"Hello jan",
                    "february":"Hello feb",
                    "march":"Hello march",
                    "april":"Hello april",
                    "may":"Hello may",
                    "june": "Hello june",
                    "july":"Hello july",
                    "august":"Hello aug",
                    "september":"Hello sept",
                    "october":"Hello oct",
                    "novermber":"Hello nov",
                    "december":None

}

# Create your views here.

# def index(request):
#     return HttpResponse("HELLO JAN")

 
# def indexi(request):
#     list_items = ""
#     months = list(monthly_challanges.keys())

#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("monthly", args=[month])
#         list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#     # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)


def indexi(request):
     
    months = list(monthly_challanges.keys())
    return render(request,'challange/index.html',{'months':months})


def monthly_challeenges_bynumbers(request,month):
    months=list(monthly_challanges.keys())
    if month>len(months):
        return HttpResponseNotFound('invalid month')
    redirect_month=months[month-1]
    redirect_path=reverse('monthly',args=[redirect_month])
    # return HttpResponseRedirect('/challanges/'+redirect_month)-when redirect path is not given
    return HttpResponseRedirect(redirect_path)


# def monthly_challenges(request,month):
#     hello=None
#     if month=="january":
#         hello='HELLO JAN'
#     elif month=="february":
#         hello='HELLLO FEB'
#     elif month=="march":
#         hello='HELLO MARCH'
#     else:
#         return HttpResponseNotFound('error')
    
#     return HttpResponse(hello)


def monthly_challanges_1(request,month):
    try:
        challange_text=monthly_challanges[month]
        # response_data=f"<h1>{challange_text}<h1> "
        response_data=render(request,'challange/challange.html',{'text':challange_text,'month_name':month})
        return HttpResponse(response_data)
    except:
        raise Http404()
        # return HttpResponseNotFound('<h1>This month is not supported <h1>')
    
 

            
    
    

    
       

 

     

    

from django.contrib import contenttypes
from django.shortcuts import render
from requests import options

from .models import Profile
import pdfkit
from  django.http import HttpResponse
from django.template import loader

# Create your views here.
def accept(request):
   
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        portfolio_site = request.POST.get('portfolio_site', '')
        linkedin = request.POST.get('linkedin', '')
        github = request.POST.get('github', '')
        twitter = request.POST.get('twitter', '')
        summary = request.POST.get('summary', '')
        education = request.POST.get('education', '')   
        skills = request.POST.get('skills', '')
        work_experience = request.POST.get('work_experience', '')
        previous_projects = request.POST.get('previous_projects', '')
        
        profile = Profile(name=name, email=email,phone=phone,portfolio_site=portfolio_site, 
                          linkedin=linkedin,github=github,twitter=twitter,summary=summary,
                          education=education,skills=skills,work_experience=work_experience,
                          previous_projects=previous_projects)
        profile.save()
        
    return render(request, 'pdf/accept.html')



""" def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template =loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    
    config = pdfkit.configuration(wkhtmltopdf="D:/wkhtmltopdf/bin/wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html,False,options, configuration=config, )
    
    #pdf = pdfkit.from_string(html,False,options)
    response = HTTPResponse(pdf, content_type="application/pdf") 
    response['content-disposition'] = 'attachment'
    filename = "resume.pdf"
    
    return response """
    
    
                    
    #old                       
    #return render(request, 'pdf/resume.html', {'user_profile': user_profile})
def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
     'page-size':'Letter',
     'encoding':"UTF-8",
     }
    config = pdfkit.configuration(wkhtmltopdf="D:/wkhtmltopdf/bin/wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html,False,options, configuration=config, )
    
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response

def list(request):
     profiles = Profile.objects.all()
     return render(request,'pdf/list.html',{'profiles':profiles})

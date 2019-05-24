from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
    response=HttpResponse()
    response.write("<html><body>\n")
    response.write("<h1>Employees Details</h1>")
    response.write("<hr>")
    elist=Employee.objects.all()
    for e in elist:
        link="<a href=\'adminapp\info\%d\'>"%(e.id)
        response.write("%s<li>%s &nbsp %s</a></li>"%(link,e.first_name,e.last_name))
        response.write("<br></body></html>")
    return response

def details(request,eid=0):
    response=HttpResponse()
    response.write("<html><body>\n")
    try:
        e=Employee.objects.get(id=eid)
        response.write("<h1>Details for Employee %s</h1><hr>\n"%e.first_name)
        response.write("<li>First name:%s</li>"%e.first_name)
        response.write("<li>Last name:%s</li>"%e.last_name)
        response.write("<li>company:%s</li>"%e.company)
        response.write("<li>email:%s</li>"%e.email)
        response.write("<li>sal:%s</li>"%e.sal)
        response.write("<li>loc:%s</li>"%e.loc)
    except Employee.DoesNotExit:
        response.write("Employee Not Found")
    response.write("</body></html>")
    return response



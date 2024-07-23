from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    rollno='2'
    name='chiku'
    pno='7978006541'
    email='adnnh@gmail.com'
    cls='9'
    st=Student(name=name, rollno=rollno,pno=pno,email=email,cls=cls)
    st.save()
    user={'rollno':rollno,'name':name,'pno':pno,'email':email,'cls':cls}
    return render(request,'home.html',user)

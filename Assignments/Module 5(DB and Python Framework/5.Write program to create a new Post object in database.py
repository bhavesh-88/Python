#What is a QuerySet?Write program to create a new Post object in database:

"""
A QuerySet is a collection of data from a database.
A QuerySet is built up as a list of objects.
QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data.
In this tutorial we will be querying data from the Members table.
"""

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks']
        )
        msg="Contact Saved Successfully"
        Contacts=Contact.objects.all().order_by("-id")[:5]
        return render(request,'contact.html',{'msg':msg},{'Contacts':Contacts})

    else:
        Contacts=Contact.objects.all().order_by("-id")[:5]
        return render(request,'contact.html',{'Contacts':Contacts})


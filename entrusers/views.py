from django.shortcuts import render
from .models import EntrepreneurUser
from .forms import EntrepreneurUserForm, RawProductForm
# Create your views here.


def entr_users_create_view(request):
    my_form = RawProductForm(request.GET)
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print("FORM CORRECT: {}".format(my_form.cleaned_data))
            EntrepreneurUser.objects.create(**my_form.cleaned_data)
        else:
            print("FORM ERROR: {}".format(my_form.errors))

    context = {
        "form": my_form
    }
    return render(request, "entrusers/entrusercreate.html", context)


def entr_users_detail_view(request):
    obj = EntrepreneurUser.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "entrusers/entruserdetail.html", context)

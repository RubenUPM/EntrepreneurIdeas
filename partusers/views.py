from django.shortcuts import render
from .models import PartnerUser
from .forms import PartnerUserForm, RawProductForm
# Create your views here.


def partner_users_create_view(request):
    my_form = RawProductForm(request.GET)
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print("FORM CORRECT: {}".format(my_form.cleaned_data))
            PartnerUser.objects.create(**my_form.cleaned_data)
        else:
            print("FORM ERROR: {}".format(my_form.errors))

    context = {
        "form": my_form
    }
    return render(request, "partusers/partusercreate.html", context)


def partner_users_detail_view(request):
    obj = PartnerUser.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "partusers/partuserdetail.html", context)

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from .models import Profile, Primary, Secondary, Tetiary, Skill_1, Skill_2, Skill_3, Interest, Experience
from .forms import contactForm


@require_http_methods(["GET", "POST"])
def home(request):
    queryset = Profile.objects.filter(featured=True)
    querysetPri = Primary.objects.filter()
    querysetSec = Secondary.objects.filter()
    querysetTet = Tetiary.objects.filter()
    querysetSki_1 = Skill_1.objects.filter()
    querysetSki_2 = Skill_2.objects.filter()
    querysetSki_3 = Skill_3.objects.filter()
    querysetInt = Interest.objects.filter()
    querysetExp = Experience.objects.filter()

    context = {
        'object_list': queryset,
        'object_listPri': querysetPri,
        'object_listSec': querysetSec,
        'object_listTet': querysetTet,
        'object_listSki_1': querysetSki_1,
        'object_listSki_2': querysetSki_2,
        'object_listSki_3': querysetSki_3,
        'object_listInt': querysetInt,
        'object_listExp': querysetExp
    }

    #    send_mail(
    #     'Appointment with ' + name,
    #     job,
    #     email,
    #     ['chukwummnl@gmail.com']
    #    )
    #    return render(request, '#section-contact', context)

    return render(request, 'index.html', context)


def contact_view(request):

    form = contactForm()

    if request.method == "POST":
        form = contactForm(request.POST)
        name = request.POST['name']
        description = request.POST['description']
        email = request.POST['email']
        if form.is_valid():
            form.save()
            send_mail(
                name,
                description,
                email,
                ['chukwummnl@gmail.com'],
                fail_silently=False
            )
            return render(request, 'msg.html')

    else:
        form = contactForm()

    return render(request, 'contact.html', {'form': form})

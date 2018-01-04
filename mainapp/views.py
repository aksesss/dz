from django.shortcuts import render
from django.core import serializers
from django.views.generic import ListView, View, FormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *


# Create your views here.
def view1(requests):
    title = "main"
    return render(requests, "base.html", locals())


class HorseListView(ListView):
    model = Horse
    # model = model.objects.filter(good_id='1')
    # list_filter = ["good_id"]
    template_name = "horses.html"
    context_object_name = "obj_list"

    # queryset = "good_id=1"

    def get(self, request, *args, **kwargs):
        self.id = request.GET.get('id')
        return super(HorseListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.id:
            return Horse.objects.filter(id=self.id)
        else:
            return Horse.objects.all()


class HorseListView1(ListView):
    model = Horse
    # model = model.objects.filter(good_id='1')
    # list_filter = ["good_id"]
    template_name = "horse.html"
    context_object_name = "obj_list"

    # queryset = "good_id=1"

    def get(self, request, *args, **kwargs):
        self.id = request.GET.get('id')
        return super(HorseListView1, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.id:
            return Horse.objects.filter(id=self.id)
        else:
            return Horse.objects.all()


def horse(request):
    id = request.GET.get('id')

    if id:
        return render(request, "horse.html", {'horse': Horse.objects.get(id=id)})
    else:
        return render(request, "horses.html", {'horses': Horse.objects.all()})


class RunView(ListView):
    form_class = RunForm
    model = Run
    template_name = "runs_list.html"
    context_object_name = "runs"
    # queryset = ['id', 'date', 'time', 'place']
    paginate_by = 3

    def get(self, request, *args, **kwargs):

        self.id = request.GET.get('id')
        self.horse_id = request.GET.get('horse')
        # form = self.form_class(request)
        if self.id:
            run_view(request)
            self.template_name = "run.html"
            self.queryset = Run.objects.filter(id=self.id)
        else:
            self.template_name = "runs_list.html"
        # return render(request, "runs_list.html", locals())
        return super(RunView, self).get(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        # form = self.form_class
        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.save()
            return HttpResponseRedirect(reverse('run_url'))
        return render(request, self.template_name, {'form': form})


def run_view(request):
    run_id = request.GET.get('id')
    if not run_id:
        return HttpResponseRedirect(reverse('runs'))
    else:
        runs = Run.objects.filter(id=run_id)
        horse_id = request.GET.get('horse')

        if request.method == 'POST':

            money = request.POST.get('money')
            if not money:
                money_error = 'Введите сумму ставки'

            u = User.objects.get(id=request.user.id)

            h = HorseInRun.objects.get(horse=horse_id, run=run_id)
            if money:
                b = Bet(user=u, amount=money, horse_in_run=h)
                b.save()
                success = True

        return render(request, "run1.html", locals())


def run_add_view(request):
    form = RunForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            # run_id = form.cleaned_data['id']
            instance = form.save(commit=False)
            # run_id = Run.objects.filter()
            # request.GET.pop(id,)
            instance.save()
            return HttpResponseRedirect(reverse('runs_url'))
    return render(request, "run_add.html", locals())



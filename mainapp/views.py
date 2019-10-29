from django.shortcuts import render
from django.core import serializers
from django.views.generic import ListView, View, FormView
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *


class RunView(ListView):
    # form_class = RunForm
    form = RunForm
    model = Run
    template_name = "runs_list.html"
    context_object_name = "runs"
    # queryset = ['id', 'date', 'time', 'place']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        run_id = request.GET.get('id')
        if not run_id:
            return super(RunView, self).get(request, *args, **kwargs)

        else:
            runs = Run.objects.filter(id=run_id)
            self.horse_id = request.GET.get('horse')
            horse_id = self.horse_id
            money_error = kwargs.get('money_error')
            return render(request, "run.html", locals())

    def post(self, request):
        run_id = request.GET.get('id')
        if not run_id:
            form = self.form(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return HttpResponseRedirect(reverse('runs_url'))
            return super(RunView, self).get(request)
        else:
            runs = Run.objects.filter(id=run_id)
            u = User.objects.get(id=request.user.id)
            h = HorseInRun.objects.get(horse=request.GET.get('horse'), run=run_id)

            money = request.POST.get('money')
            money_error = ""
            if not money or money == "0":
                money_error = 'Введите сумму ставки'
            else:
                if float(money) > float(u.cash):
                    money_error = 'У вас на счету всего ' + str(u.cash) + ' рублей'

                else:
                    b = Bet(user=u, amount=money, horse_in_run=h)
                    u.cash = u.cash - float(money)
                    u.save()
                    b.save()
            return self.get(request,money_error=money_error)
            # return render(request, "run.html", locals())


class RunView1(ListView):
    form_class = RunForm
    model = Run
    template_name = "runs_list1.html"
    context_object_name = "runs"
    paginate_by = 1


def run_add_view(request):
    form = RunForm(request.POST or None, request.FILES or None)
    print(form.as_p())
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('runs_url'))
    return render(request, "run_add.html", locals())


def view1(requests):
    title = "main"
    return render(requests, "base.html", locals())


class HorseListView(ListView):
    model = Horse
    template_name = "horses.html"
    context_object_name = "obj_list"

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
    template_name = "horse.html"
    context_object_name = "obj_list"

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

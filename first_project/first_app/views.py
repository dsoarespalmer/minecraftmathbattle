from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from first_app.models import Topic,Webpage,AccessRecord,RandoNum
from first_app import forms
# Create your views here.
import random
print("Random integer is", random.randint(0, 10))

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html',context=date_dict)

def index(request):
    num_dict = {'num1':str(random.randint(0, 10)),'num2':str(random.randint(0, 10))}
    return render(request, 'first_app/index.html',context=num_dict)

def add(request):

    num_dict = {'num1':str(random.randint(0, 5)),'num2':str(random.randint(1, 5)), 'mob_score':str(6), 'player_score':str(6)}
    num1 = randint(0,5)
    num2 = randint(1,5)
    mob_score = 6
    player_score = 6

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        old_player_score = request.POST['old_player_score']
        old_mob_score = request.POST['old_mob_score']

        #Error handling if empty form submitted
        if not answer:
            my_answer = "You didn't submit an answer!"
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))
            return render(request, 'first_app/add.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color':color,
                'player_score':player_score,
                'mob_score':mob_score,
                })
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + str(old_num1) + " + " + str(old_num2) + " = " + str(int(correct_answer))
            color = "success"
            mob_score = str(int(old_mob_score) -1)
            player_score = str(int(old_player_score))
        else:
            my_answer = "Incorrect! " + str(old_num1) + " + " + str(old_num2) + " = " + str(int(correct_answer)) + ", not " + str(answer)
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))

        return render(request, 'first_app/add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color':color,
            'player_score':player_score,
            'mob_score':mob_score,
            })
    return render(request, 'first_app/add.html', context=num_dict)
    return render(request, 'first_app/add.html', {})

def subtract(request):
    num1 = randint(1,10)
    num2 = randint(0,num1)
    num_dict = {'num1':str(num1),'num2':str(num2), 'mob_score':str(6), 'player_score':str(6)}

    mob_score = 6
    player_score = 6

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        old_player_score = request.POST['old_player_score']
        old_mob_score = request.POST['old_mob_score']

        #Error handling if empty form submitted
        if not answer:
            my_answer = "You didn't submit an answer!"
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))
            return render(request, 'first_app/subtract.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color':color,
                'player_score':player_score,
                'mob_score':mob_score,
                })

        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + str(old_num1) + " - " + str(old_num2) + " = " + str(int(correct_answer))
            color = "success"
            mob_score = str(int(old_mob_score) -1)
            player_score = str(int(old_player_score))
        else:
            my_answer = "Incorrect! " + str(old_num1) + " - " + str(old_num2) + " = " + str(int(correct_answer)) + ", not " + str(answer)
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))

        return render(request, 'first_app/subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color':color,
            'player_score':player_score,
            'mob_score':mob_score,
            })
    return render(request, 'first_app/subtract.html', context=num_dict)
    return render(request, 'first_app/subtract.html', {})


def multiply(request):
    num_dict = {'num1':str(random.randint(0, 12)),'num2':str(random.randint(0, 12)), 'mob_score':str(6), 'player_score':str(6)}
    num1 = randint(0,12)
    num2 = randint(0,12)
    mob_score = 6
    player_score = 6

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        old_player_score = request.POST['old_player_score']
        old_mob_score = request.POST['old_mob_score']

        #Error handling if empty form submitted
        if not answer:
            my_answer = "You didn't submit an answer!"
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))
            return render(request, 'first_app/multiply.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color':color,
                'player_score':player_score,
                'mob_score':mob_score,
                })

        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + str(old_num1) + " x " + str(old_num2) + " = " + str(int(correct_answer))
            color = "success"
            mob_score = str(int(old_mob_score) -1)
            player_score = str(int(old_player_score))
        else:
            my_answer = "Incorrect! " + str(old_num1) + " x " + str(old_num2) + " = " + str(int(correct_answer)) + ", not " + str(answer)
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))

        return render(request, 'first_app/multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color':color,
            'player_score':player_score,
            'mob_score':mob_score,
            })
    return render(request, 'first_app/multiply.html', context=num_dict)
    return render(request, 'first_app/multiply.html', {})


def divide(request):
    #num3 = randint(1,12)
    #num2 = randint(1,12)
    #num1 = num2 * num3
    #num_dict = {'num3':str(random.randint(1, 12)),'num2':str(random.randint(1, 12)), 'num1':(num2*num3), 'mob_score':str(6), 'player_score':str(6)}
    #mob_score = 6
    #player_score = 6

    num3 = randint(1, 12)
    num2 = randint(1, 12)
    num1 = num2 * num3
    num_dict = {'num3':str(num3),'num2':str(num2), 'num1':str(num1), 'mob_score':str(6), 'player_score':str(6)}
    mob_score = 6
    player_score = 6

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        old_player_score = request.POST['old_player_score']
        old_mob_score = request.POST['old_mob_score']

        #Error handling if empty form submitted
        if not answer:
            my_answer = "You didn't submit an answer!"
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))
            return render(request, 'first_app/divide.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'num3': num3,
                'color':color,
                'player_score':player_score,
                'mob_score':mob_score,
                })

        correct_answer = int(old_num1) / int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + str(old_num1) + " / " + str(old_num2) + " = " + str(int(correct_answer))
            color = "success"
            mob_score = str(int(old_mob_score) -1)
            player_score = str(int(old_player_score))
        else:
            my_answer = "Incorrect! " + str(old_num1) + " / " + str(old_num2) + " = " + str(int(correct_answer)) + ", not " + str(answer)
            color = "danger"
            player_score = str(int(old_player_score) -1)
            mob_score = str(int(old_mob_score))

        return render(request, 'first_app/divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'num3': num3,
            'color':color,
            'player_score':player_score,
            'mob_score':mob_score,
            })
    return render(request, 'first_app/divide.html', context=num_dict)
    return render(request, 'first_app/divide.html', {})

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("validation success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
            print("Answer: "+str(form.cleaned_data['answer']))

    return render(request, 'first_app/formpage.html',{'form':form, 'num1':str(random.randint(0, 10)),'num2':str(random.randint(0, 10))})

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, User_Register,IMG
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def user_msg(request, user_id):
    # 已有的msg
    user_msg = get_object_or_404(User_Register, pk=user_id)
    return render(request, 'polls/user_msg.html', {'user_msg': user_msg})

def user_msg_create(request):

    return render(request, 'polls/add_user.html', {'user_msg': user_msg})

def user_msg_add(request):
    # 已有的msg
    # user_msg = get_object_or_404(User_Register, pk=user_id)
    name = request.POST['name']
    email = request.POST['email']
    payment = request.POST['payment']
    user_msg=User_Register(name=name,email=email,payment=payment)
    user_msg.save()
    return HttpResponse("You're add succeed %s." % name)

def user_msg_change(request, user_id):

    user_msg = get_object_or_404(User_Register, pk=user_id)
    name = request.POST['name']
    email = request.POST['email']
    payment = request.POST['payment']

    user_msg.name=name
    user_msg.email=email
    user_msg.payment=payment
    user_msg.save()

    return HttpResponse("You're change succeed %s." % name)

def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name,
            gender=request.POST['gender']
        )
        sss= request.FILES.get('img')
        ppp=sss.size
        new_img.save()
    return render(request, 'polls/uploadimg.html')

def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'polls/showimg.html', content)
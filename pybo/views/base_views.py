from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
import logging
logger = logging.getLogger('pybo')
# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    logger.info("INFO Level Output")
    # 입력 파라미터
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    #페이징처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    #context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)

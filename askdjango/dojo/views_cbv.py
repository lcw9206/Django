from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse, JsonResponse

class PostListView1(View):
    'CBV: 직접 문자열로 HTML형식 응답하기'

    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}입니다.</p>
        '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    'CBV: 템플릿을 통해 HTML형식 응답하기'

    template_name = 'dojo/post_list2.html'

    # 인자 넘기기
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()


class PostListView3(View):
    'CBV: JSON 형식 응답하기'
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})
    def get_data(self):
        return {
                'message': '안녕, 파이썬&장고',
                'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'], }

post_list3 = PostListView3.as_view()




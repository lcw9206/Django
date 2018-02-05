# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Candidate, Poll, Choice 	# row를 불러오기 위한 import
from django.db.models import Sum
import datetime

def index(request):
	candidates = Candidate.objects.all()  # 변수candidates에 Candidate 테이블의 모든 row를 할당한다.
	context = {'candidates': candidates}
	return render(request, 'elections/index.html', context)	# 요청을 넘겨받아 render 메서드로 context 값을 전달한 후, html을 보여준다(return).

def areas(request, area):
	today = datetime.datetime.now()	# 현재 시간 가져오기
	try:
		poll = Poll.objects.get(area = area,start_date__lte = today,	# start date < 오늘 < end date
			end_date__gte=today)
		candidates = Candidate.objects.filter(area = area)	# 동일한 지역구의 후보자들만 불러온다.
	except:
		poll = None
		candidates = None
	context = {'candidates': candidates,
	'area' : area,
	'poll' : poll}
	return render(request, 'elections/area.html', context)

def polls(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)		# Poll 객체를 구분하는 주요 키가 poll_id인 객체를 poll 변수에 할당한다.
	selection = request.POST['choice']		# 사용자가 선택한 값 (area.html에서 button name)

	try:
		choice = Choice.objects.get(poll_id = poll_id, candidate_id =
			selection)
		choice.votes += 1
		choice.save()
	except:
		choice = Choice(poll_id = poll_id, candidate_id = selection, votes = 1)
		choice.save()

	return HttpResponseRedirect("/areas/{}/results".format(poll.area))

def results(request, area):
	candidates = Candidate.objects.filter(area = area)
	polls = Poll.objects.filter(area = area)
	poll_results = []
	for poll in polls:
		result = {}
		result['start_date'] = poll.start_date
		result['end_date'] = poll.end_date
		total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))	# id에 맞는 투표 수 가져와 Sum을 한다. /import 해야한다.
		result['total_votes'] = total_votes['votes__sum']
		rates = []
		for candidate in candidates:
			try:
				choice = Choice.objects.get(poll = poll.id,
					candidate = candidate.id)
				rates.append(round(choice.votes * 100 / result['total_votes'],1))
			except:
				rates.append(0)
		result['rates'] = rates
		poll_results.append(result)

	context = {'candidates' : candidates, 'area' : area,
	'poll_results' : poll_results}

	return render(request, 'elections/result.html', context)
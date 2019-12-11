# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
post =[
	{
		'title': 'Mont Black',
		'user': {

			'name': 'Yesica Cortes',
			'picture': 'https://picsum.photos/id/1027/60/60'
		},
		'timestamp':  datetime.now().strftime('%b %dth , %Y - %H:%M hrs '),
		'photo':'https://picsum.photos/id/1036/800/600'
	},
		{
		'title': 'Via Lactea',
		'user': {

			'name': 'Christian Van der Henst',
			'picture': 'https://picsum.photos/id/903/60/60'
		},
		'timestamp':  datetime.now().strftime('%b %dth , %Y - %H:%M hrs '),
		'photo':'https://picsum.photos/id/903/800/800'
	},
		
			{
		'title': 'Nuevo Auditorio',
		'user': {

			'name': 'Uriel (thepianartist)',
			'picture': 'https://picsum.photos/id/883/60/60'
		},
		'timestamp':  datetime.now().strftime('%b %dth , %Y - %H:%M hrs '),
		'photo':'https://picsum.photos/id/1076/500/700'
	},
		
		

]

def listPost(request):

	# content = []

	# for posts in post:
	# 	content.append("""
	# 		<p><strong>{name}</strong></p>
	# 		<p><small>{user} - <i>{timestamp}</i></small></p>
	# 		<figure><img src="{picture}"></figure>
	# 		""".format(**posts))


	# return HttpResponse('<br>'.join(content))
	return render(request, 'feed.html', {'post': post})


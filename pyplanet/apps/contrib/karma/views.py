from pyplanet.apps.core.maniaplanet.models import Map

from pyplanet.views.generics.list import ListView


class SampleListView(ListView):
	model = Map
	query = Map.select()
	fields = [
		{
			'name': 'Name',
			'index': 'name',
			'sorting': True,
			'searching': True,
			'width': 100,
		},
		{
			'name': 'Author',
			'index': 'author_login',
			'sorting': True,
			'searching': True,
			'renderer': lambda row, field:
				row.author_nickname if row.author_nickname and len(row.author_nickname) > 0 else row.author_login,
			'width': 50,
		},
	]
	title = 'Map List Testing'

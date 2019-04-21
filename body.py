import json
class Response(dict):

	__setattr__= dict.__setitem__  # TBD: support assignment of nested dicts by overriding this?
	__delattr__= dict.__delitem__
	
	def __init__(self, data):
		if type(data) == str:
			data = json.loads(data)
			
		for name, value in data.items():
			setattr(self, name, self._wrap(value))

	def __getattr__(self, attr):
		return self.get(attr, None)
		
	def _wrap(self, value):  # Reff http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
		if isinstance(value, (tuple, list, set, frozenset)):
			return type(value)([self._wrap(v) for v in value])
		else:
			if isinstance(value, dict):
				return Response(value)
			else:
				return value

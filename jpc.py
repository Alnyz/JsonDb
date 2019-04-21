import json
from body import Response
from typing import Any

class Jpc:
	def __init__(self, files):
		self.files = files
		op = open(self.files, "r").read()
		if "{" not in op or "}" not in op and len(op) < 3:
			json.dump({}, open(self.files, "w"))		
		self.reads = Response(open(self.files, "r").read())

	def is_exist(self, key: str) -> bool:
		r = self.reads
		if key in r.keys():
			return True
		return False

	def add(self, key: str, data: Any) -> bool:
		r = self.reads
		if self.is_exist(key):
			raise Exception("Duplicate key, {} key already exist!".format(key))
		json.dump({key:data}, open(self.files, "w"), indent=4)

	def purge(self) -> bool:
		r = self.reads
		if r == {}:
			raise Exception("File already empty!")
		r = {}
		json.dump(r, open(self.files, "w"))
		return True

	def delete(self, key: str) -> bool:
		r = self.reads
		if not self.is_exist(key):
			raise AttributeError("key {} not found in data".format(key))
		del r[key]
		json.dump(r, open(self.files, "w"), indent=4)

	def update(self, key:str, data: Any) -> bool:
		r = self.reads
		if not self.is_exist(key) and r != {}:
			raise AttributeError("key {} not found in data".format(key))
		if r == {}:
			r.update({key:data})
		else:
			r[key] = data
		json.dump(r, open(self.files, "w"), indent=4)
		return True

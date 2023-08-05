import re

class NoTrans:

	_sexes = {
		"male": "male",
		"female": "female"
	}
	
	_genders = {
		"adult": {
			"singular": { "male": "man", "female": "woman" },
			"plural": { "male": "men", "female": "women" }
		},
		"child": {
			"singular": { "male": "boy", "female": "girl" },
			"plural": { "male": "boys", "female": "girls" }
		}
	}
	
	_regexes = {
		"parser": re.compile(r"\b(?:(trans|cis)(?:\s*|-?)(?:gender(?:ed)?)?)(?:\s*|-)((?:(?:wo)?m[ae]n)|boys?|girls?)\b", re.I),
		"man": re.compile(r"^m[ae]n$", re.I),
		"woman": re.compile(r"^wom[ae]n$", re.I),
		"boy": re.compile(r"^boys?$", re.I),
		"girl": re.compile(r"^girls?$", re.I),
		"cis": re.compile(r"^cis$", re.I),
		"trans": re.compile(r"^trans$", re.I),
		"plural": re.compile(r"(?:en|s)$", re.I)
	}

	def __init__(self, isomer: str, designator: str):
		self.isMan = bool(self._regexes["man"].search(designator))
		self.isWoman = bool(self._regexes["woman"].search(designator))
		self.isBoy = bool(self._regexes["boy"].search(designator))
		self.isGirl = bool(self._regexes["girl"].search(designator))
		self.isCis = bool(self._regexes["cis"].search(isomer))
		self.isTrans = bool(self._regexes["trans"].search(isomer))
		self.isPlural = bool(self._regexes["plural"].search(designator))
		
	@classmethod
	def _invertGender(cls, g: str) -> str|None:
		if(g == cls._genders["adult"]["singular"]["female"]):
			return cls._genders["adult"]["singular"]["male"]
		elif(g == cls._genders["adult"]["singular"]["male"]):
			return cls._genders["adult"]["singular"]["female"]
		elif(g == cls._genders["child"]["singular"]["female"]):
			return cls._genders["child"]["singular"]["male"]
		elif(g == cls._genders["child"]["singular"]["male"]):
			return cls._genders["child"]["singular"]["female"]
		elif(g == cls._genders["adult"]["plural"]["female"]):
			return cls._genders["adult"]["plural"]["male"]
		elif(g == cls._genders["adult"]["plural"]["male"]):
			return cls._genders["adult"]["plural"]["female"]
		elif(g == cls._genders["child"]["plural"]["female"]):
			return cls._genders["child"]["plural"]["male"]
		elif(g == cls._genders["child"]["plural"]["male"]):
			return cls._genders["child"]["plural"]["female"]
		else:
			return None		
		
	@classmethod
	def _invertSex(cls, s: str) -> str|None:
		if(s == cls._sexes["male"]):
			return cls._sexes["female"]
		elif(s == cls._sexes["female"]):
			return cls._sexes["male"]
		else:
			return None
			
	@classmethod
	def _pluralizeGender(cls, g: str) -> str|None:
		if(g == cls._genders["adult"]["singular"]["female"]):
			return cls._genders["adult"]["plural"]["female"]
		elif(g == cls._genders["adult"]["singular"]["male"]):
			return cls._genders["adult"]["plural"]["male"]
		elif(g == cls._genders["child"]["singular"]["female"]):
			return cls._genders["child"]["plural"]["female"]
		elif(g == cls._genders["child"]["singular"]["male"]):
			return cls._genders["child"]["plural"]["male"]
		else:
			return None
			
	@classmethod
	def replaceAll(cls, instr: str, cb: callable = None) -> str:
		def repl(m):
			p = cls(m.group(1), m.group(2))
			return cb(m.group(0), p) if callable(cb) else str(p)
		return cls._regexes["parser"].sub(repl, instr)
	
	@classmethod
	def matchCase(cls, str1: str, str2: str) -> str:
		
		isAllCaps = len(str1) > 0 and str1.isupper()
		isTitle = not isAllCaps and len(str1) > 0 and str1[0].isupper()
		
		if(isAllCaps):
			str2 = str2.upper()
		elif(isTitle):
			str2 = str2[0].upper() + str2[1:]
			
		return str2
		
	def getSex(self) -> str|None:
		
		sx = None
		
		if(self.isWoman or self.isGirl):
			sx = self._sexes["female"]
		elif(self.isMan or self.isBoy):
			sx = self._sexes["male"]
		
		if(self.isTrans):
			sx = self._invertSex(sx)
			
		return sx
		
	def getTi(self) -> str:
		if(self.isTrans):
			return "trans-identified {}".format(self.getSex())
		return None
		
	def getGender(self) -> str|None:
		
		g = None
		
		if(self.isWoman):
			g = self._genders["adult"]["singular"]["female"]
		elif(self.isMan):
			g = self._genders["adult"]["singular"]["male"]
		elif(self.isGirl):
			g = self._genders["child"]["singular"]["female"]
		elif(self.isBoy):
			g = self._genders["child"]["singular"]["male"]
		else:
			return None
			
		if(self.isTrans):
			g = self._invertGender(g)
			
		if(self.isPlural):
			g = self._pluralizeGender(g)
			
		return g
		
	def __str__(self):
		return self.getGender()

from getID import getID

string = "string"

def test():
	ids = getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")
	for i in ids:
		return i
	print len(ids)

print test()

#if type(test()) == type(string):
#	print True

#else: 
#	print False
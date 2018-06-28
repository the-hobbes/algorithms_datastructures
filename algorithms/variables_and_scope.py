def changeInt(i):
	i = 0

def changeStr(s):
	s = 'yo'

def changeList(l):
	l.append(10)

def main():
	i = 10
	changeInt(i)
	assert i == 10
	s = 'hello'
	changeStr(s)
	assert s == 'hello'
	l = []
	changeList(l)
	assert l == [10]

if __name__ == '__main__':
	main()

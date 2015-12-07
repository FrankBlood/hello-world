print("Hello world!")
def normalize(name):
	return name.capitalize()

L1=['adam','LISA','BarT']
L2=list(map(normalize,L1))
print(L2)
a=input('a=')
b=input('b=')
print('a+b=',a+b)
name=input('Please enter your name:')
print('hello,',name)

def abs(a):
	if a>=0:
		print(a)
	else:
		print(-a)
a=input('a=')
abs(a)
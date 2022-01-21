s=1
n=1
nc=1
d=[]
dc=[]
while s:  
    x=input('Write a word : (dc for list of Palindrome words\n                d for list of other entry words)\n-->')
    y=x[::-1]
    #print(x,'\n',y)
    if x==y:
    	print('{} it\'s Palindrome word'.format(x))
    	dc.append(x)
    	nc+=1
    else:
    	print('it\'s not a Palindrome word\ntry another word')
    	d.append(x)
    	n+=1
    if x=='dc':
    	print(dc)
    	d.remove(x)
    elif x=='d':
    	print(d)
    	dc.remove(x)
    s=int(input('0 for exit or num for contine'))
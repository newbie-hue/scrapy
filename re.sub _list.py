import re

ex_list = ['\3','\3',' ','mklmlkm','mkmkml']

a = filter(lambda x:re.sub("\3",'',x).strip(),ex_list)

print("".join(list(a)))

b = '%(spider)s:items' % {'spider':'eccecrcerc'}
print(b)

c = {
    'body':None,
}

d = c['body'] or b''
print(d)
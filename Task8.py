t=sorted('И, Н, С, Т, А, В, К'.split(', '))
l=[]
for i1 in t:
   for i2 in t:
       for i3 in t:
           for i4 in t:
               if i1 in 'НСТВК' and i4 in 'ИА':
                   l.append(i1+i2+i3+i4)
item = 'НИКА'
index = l.index(item)
print ("Ответ:", index+1)

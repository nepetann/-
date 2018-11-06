disk = 2# к-во дисков
kernel = 3# к-во стержней
aa=[]
pos=[]
for i in range(0,disk):
  aa.append(0)
for i in range(0,kernel):
  pos.append(aa) 
#позиция: номер стержня и диски на нем
print (pos)
for i in range(0,disk): #заполнили 0-ой стержень (первонач пирамидка)
  pos[0][i]=disk-i
print(pos)
end=[]
end.append(disk-1)# массив индексов последних элементов
for i in range(1,kernel):
  end.append(-1)
print (end)
def foo(numb, end, disk, kernel, pos):
  #numb - номер стержня с которого берем верхний диск
  #далее перемещаем диск на другой стержень
  c_numb=pos[numb][end[numb]]
  pos[numb][end[numb]]=0
  end[numb]-=1
  for i in range(0,kernel):

    if (pos[i][end[i]]>c_numb) and (i!=numb) :
      pos[i][end[i]+1]=pos[numb][end[numb]]
    
      foo(i,end,disk,kerl)
      for i in range(0,kernel):
        if end[i]==disk-1:
          return pos
  return pos
      

pos=foo(0,end,disk,kernel,pos)
for i in range(0,kernel):
  if end[i]!=-1:
    print (i,'стержень -',pos[i])

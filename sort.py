
def foo(ind1,ind2,arr):
  new_arr=[]
  if (ind2-ind1)==1:
    new_arr=[]
    new_arr.append(min(arr[ind1],arr[ind2]))
    new_arr.append(max(arr[ind1],arr[ind2]))
    return (new_arr)
  if (ind2-ind1)==0:
    return (arr[ind1])

  ind12=ind1+(ind2-ind1+1)//2
  arr1=foo(ind1,ind12-1,arr)
  arr2=foo(ind12,ind2,arr)
  #for i1,i2 in range(ind1,ind12-1),range(ind12,ind2):
  #  new_arr.append(min(arr1[i1],mas[i2]))
  #  new_arr.append(max(mas[i1],mas[i2]))
  
  for i in range(0,len(arr1)):
    new_arr.append(min(arr1[i],arr2[i]))
    new_arr.append(max(arr1[i],arr2[i]))

  return new_arr

mas=[38,27,43,3,9,82,10,11]

mas=foo(0,len(mas)-1,mas)
for item in mas:
  print(item)

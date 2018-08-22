def getList(oldList,length):
  #'oldList = [1]'
    if int(length) > 0:
        for i in range(length):
            oldList.append(i)
        return  oldList
    else:
        return 'Your input lenght less than zero!'
print getList([1],10)

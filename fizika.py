fizika = [2,3,2,2,3,3,3]
fizika.count(2)
def fizika1():
      for i in range(fizika.count(2)):
            
            fizika.remove(2)

            
      for j in range(fizika.count(3)):
            i = fizika.index(3)
            fizika.pop(i)
            fizika.insert(i,4)
            

      for p in range(fizika.count(4)):
            i = fizika.index(4)
            fizika.pop(i)
            fizika.insert(i,5)  
      print (fizika)


fizika1()    



      





      
      
      
      

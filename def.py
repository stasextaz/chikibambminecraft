import math
def ahaha (a,b,c):
      if ((b * b - 4 * a * c) < 0) :
            print ("из отрицательного дискриминанта нельзя вычеслить корень")
      
      
      
      
      else:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2*a)
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2*a)
            print(x1)
            print(x2)
ahaha (5,-6,14)



      
     




def countdown(n):
     if n <= 0:
          print('Action!')
     else:
          print(n)
          countdown(n-1)

def countup(n):
     if n >= 0:
          print('Action!')
     else:
          print(n)
          countup(n+1)

n = int(input('Enter a negative or positive number: '))

if n > 0:
     print(n)
     countdown(n-1)
if n == 0:
     print('Action!')
if n < 0:
    print(n)
    countup(n+1)


    
    


    


    

           


          
          





          

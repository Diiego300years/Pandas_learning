# Program to print Multiplication
# table of a Number

# set_trace() call to pdb module
import pdb

pdb.set_trace()

n=5
for x in range(1,11) :
  print( n , '*' , x , '=' , n*x )


"""
Czyli tak list 1,5 wświelta linie 1-5
break lub b 9 ustawia breakpoint na linii 9, continue aby ją wykonać
c lub continue wykonuje kod
pp x lub pp n wyświetla co kryje sie pod ta zmienna
cl - usuwa wszystkie breakpointy
quit/exit wychodzisz
help wypisuje wszystkie komendy

"""




x = [n for n in range(10) if n%2 == 0]
print(x)
print("/////////////////////////////////////")

g = lambda f: f*f*f
xyz = [g(f) for f in range(10)]

print(xyz)

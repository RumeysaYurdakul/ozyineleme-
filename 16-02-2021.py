#öz yinelemeli fonksiyon örneği
#16.02.2021
def hepyaz(m,s):
     
     if s==100:
          print(" geri dönüyoruz")
     else:
          print(m,s)
          hepyaz(m,s+1)
          print(s,".çağrı sonlanmak üzere")
     return "bitti"


#ana program
sonuc=hepyaz("merhaba",1)
print(sonuc)

for a in range(0,10):
   for b in range(0,10):
     for c in range(0,10):
       for d in range(0,10):
         if (d + (c*10 + d) + (b*100 + c*10 + d) + (a*1000 + b*100 + c*10 + d) == 2222):
           print("Solution:")
           print("a: " + str(a))
           print("b: " + str(b))
           print("c: " + str(c))
           print("d: " + str(d))
           print("---------")

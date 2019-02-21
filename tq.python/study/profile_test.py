import cProfile

def profileTest():
   Total =1;
   for i in range(10):
       Total=Total*(i+1)
       print(Total)
   return Total
if __name__ == "__main__":
    cProfile.run("profileTest()")
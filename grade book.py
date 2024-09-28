eng=int(input("what is your English marks ? "))
math=int(input("what is your Math marks ? "))
sci=int(input("what is your Science marks ? "))
total=(eng+math+sci)

percent=(total/300)*100


if 80<=percent:print(f"Grade:A+ percent:{percent} GPA:5")
      
        
elif 70<=percent:print(f"Grade:A percent:{percent}")
    

elif 60<=percent:print(f"Grade:A- percent:{percent}")
    

elif 50<=percent:print(f"Grade:B percent:{percent}")
    
elif 33<=percent:print(f"Grade:B- percent:{percent}")
    
else:print("GRADE: F PERCENT :0")
    

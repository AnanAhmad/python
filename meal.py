def main():
    ans=input("what time is it ? ")
    time=convert(ans)
    
    if ans .endswith("am") and time>=7 or time<=8:
        print("breakfast time")
   
    



def convert(time):
    h,m,t=time.split(": ")
    M=float(m)/60
    return float(h)+M 


if __name__ == "__main__":
    main()
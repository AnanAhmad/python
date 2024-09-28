x = input("What is the Answear to the  Great Question of Life, the Universe and Everything :").lower()
match x.strip():
    case "42"| "forty two" |"forty_two":
     print("yes")

    case _: 
         print("no")
   
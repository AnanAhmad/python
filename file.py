file=input("File name:").lower()
if file.endswith('.gif'): 
   print("image/gif")

elif file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith("jpeg"):
    print("image/jpeg")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
elif file.endswith(".png"):
    print("image/png")

   
with open("artifacts_01.txt","r") as f:
    text = f.read()
    
print(text)

with open("artifacts_02.txt","w") as f:
    text = f.write(text + "Added lines")
    
print("end of stage 3")
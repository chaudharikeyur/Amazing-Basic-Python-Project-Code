
def getdailymeal(food,name):
     print("You have to eat {}".format(food),name)
     md = getdate()
     print(md)
     file1 = open("HMS.txt", "a")
     fi = file1.write("***"+name+"***"+"\nYou have to eat {}".format(food)+" "+name)
     file1.close()

def getexercises(exercise,name):
    print("You have to do  {}".format(exercise),name)
    dh = getdate()
    print(dh)
    file1 = open("HMS.txt", "a")
    fi = file1.write( "\nYou have to do {}".format(exercise) +" "+ name + "\n\nTHANK YOU FOR VISITING\n\n")
    file1.close()

def getdate():
    import datetime
    return datetime.datetime.now()

while True:
     name1= input("Enter the name of guy for which you want to set routine:\n 1)Rohan\n 2)Ross\n 3)Rony \n")

     ch = input("Do You want add meal? : \n 1)Yes \n 2)No \n")
     if ch == 'Yes':
         h = input("which meal do you want to add?\n")
         getdailymeal(h,name1)

         ch1 = input("Do you want to add Exercise too? : \n 1)Yes \n 2)No \n")
         if ch1 == 'Yes':
              g = input("which exercise do you want to add in routine?\n")
              getexercises(g,name1)



     choice = input("do you want to continue: yes/no\n")
     if choice == 'no' or choice == 'n':
         break






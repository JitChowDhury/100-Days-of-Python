#FileNotFoundError
# with open("a_fule.txt") as file: #this file doesnt exist
#   file.read()

#keyError
# demo_dict = {"key1" : "value1"}
# print(demo_dict["nonexistentkey"])

#typeError
# text="abc"
# print(5+text)

#indexError
# demo_list=[1,2,3]
# print(demo_list[4])

# try:
# something that might cause an exception
# except:
# do this if there is an exception
# else:
# do this if there was no exception
# finally:
# do this no matter what happens



# try:
#   file = open("E:/CODE/100 days of Code-Python/Day-30/a_file.txt")
#   new_dict={"key":"value"}
#   print(new_dict["key"])
# except FileNotFoundError as errorM:
#   print(errorM)
#   file=open("E:/CODE/100 days of Code-Python/Day-30/a_file.txt","w")
#   file.write("Something")
# except KeyError as errorM:
#   print(errorM)
# else:
#   content = file.read()
#   print(content)
# finally:
#   raise KeyError("THis is and Keyerror")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height>3:
  raise ValueError("HUman Height???? WTF")

bmi=weight/height**2
print(bmi)
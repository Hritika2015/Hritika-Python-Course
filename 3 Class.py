print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english:"))
science = int(input("science:"))
RE = int(input("RE:"))
sum = math+english+science+RE
print (" sum of math,english,science and RE")
perc = (sum/400)*100
print (end="Percentage Mark = ")
print(perc)
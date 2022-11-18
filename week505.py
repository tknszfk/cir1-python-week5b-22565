#mark = 0
mark = int(input("Enter score: "))
if mark >= 80: and mark <= 100:   #80 to 100
    print(mark,": GRADE is A")
elif mark >=70: and mark <= 80:   #70 to 79
    print(mark,": GRADE is B")
elif mark >=60: and mark <= 70:   #60 to 69
   print(mark,": GRADE is C")    
elif mark >=50: and mark <= 60:    #50 to 59
   print(mark,": GRADE is D")
elif mark >=40: and mark <= 50:    #0 to 49
   print(mark,": GRADE is E")
else
    print(mark,": GRADE is ERROR")
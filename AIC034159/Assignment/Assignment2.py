# Write a program to calculate the percentage of a student and generate a report card of the student

# This is the code to calculate the percentage of the student
# Total marks of the total subjects
totalMarks = 550

# User input of usr info and all the mark a student obtained
name = input("Enter student name: ")
rollNumber = input("Enter roll number: ")
english = float(input("Enter English course number: "))
urdu = float(input("Enter Urdu course number: "))
mathematics = float(input("Enter Mathematics course number: "))
islamiyat = float(input("Enter Islamiyat course number: "))
pakistanStudies = float(input("Enter PakistanStudies course number: "))
science = float(input("Enter Science course number: "))

# Calculate the marks obtained
marksObtained = (english + urdu + mathematics + islamiyat + pakistanStudies + science)
# Calculate percentage
percentage = ((marksObtained / totalMarks) * 100)

# Print format of the report
print("\n===========================================================================")
print("                               Report Card")
print("===========================================================================\n")
print("Name: " + name)
print("Roll No.: " + rollNumber)
print("\n===========================================================================")
print("Subject              Total Marks         Obtained Marks          Percentage")
print("===========================================================================")
print("English              100                 "+str(round(english, 2))+"                    "+str(round(english/100*100, 2))+"%")
print("Urdu                 100                 "+str(round(urdu, 2))+"                     "+str(round(urdu/100*100, 2))+"%")
print("Mathematics          100                 "+str(round(mathematics, 2))+"                     "+str(round(mathematics/100*100, 2))+"%")
print("Islamiyat            50                  "+str(round(islamiyat, 2))+"                     "+str(round(islamiyat/50*100, 2))+"%")
print("Pakistan Studies     100                 "+str(round(pakistanStudies, 2))+"                    "+str(round(pakistanStudies/100*100, 2))+"%")
print("Science              100                 "+str(round(science, 2))+"                     "+str(round(science/100*100, 2))+"%")
print("===========================================================================")

# Print Total 
print("Total                550                 "+str(round(marksObtained, 2))+"                   "+str(round(percentage, 2)))

# Print the grade with respect to the percentage
if(percentage >= 90):
    print("Grade A1")
elif (percentage >= 80):
    print("Grade A")
elif (percentage >= 70):
    print("Grade B")
elif (percentage >= 60):
    print("Grade C")
elif (percentage > 50):
    print("Grade D")
else:
    print("Fail")
print("===========================================================================\n")
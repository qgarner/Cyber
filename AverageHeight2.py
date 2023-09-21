student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = sum(student_heights)
total_students = len(student_heights)
average_height = round(total_height/total_students)
print(average_height)
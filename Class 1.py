marks = []

for i in range(5):
    mark = int(input(f"Enter the {i+1}th mark: "))
    marks.append(mark)

total = sum(marks)
avg = total / 5

print("Marks:", marks)
print("Sum of marks:", total)
print("Average of marks:", avg)

if avg>=80:
    print("A")
elif avg>=65 and avg<80:
    print("B")
elif avg>=50 and avg <65:
    print("C")
elif avg>40 and avg<50:
    print("D")
else:
    print("Fail")

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
# Current Number 0 Previous Number  0  Sum:  0
previous_sum = 0
for i in range(10):
    sum = i + previous_sum
    print("Current Number", i, "Previous Number", previous_sum, "Sum", sum)
    previous_sum = i
    
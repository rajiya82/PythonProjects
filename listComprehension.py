

# list Comprehension - print only even numbers

numbers = [1,2,3,4,5,6,7,8,9]
evens = [number for number in numbers if number % 2 == 0]
print(evens)

lables  = ["even" if number %2 == 0 else "odd" for number in numbers]
print(lables)

matrix = [[1,2],[3,4],[5,6],[7,8]]
flatterened  = [num for row in matrix for num in row]
print(flatterened)
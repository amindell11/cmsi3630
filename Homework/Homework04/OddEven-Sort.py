def oddeven_sort():
    
   input_string = input("Enter numbers seperated by spaces: ")
   input_array = list(map(int, input_string.split()))

   even_array = []
   odd_array = []
   
#This block of code does the dirty work this is where things get done   
   for num in input_array:
      if num % 2 == 0:
         even_array.append(num)
      else:
         odd_array.append(num)

   return even_array, odd_array

#This does the boring ole sort
even_numbers, odd_numbers = oddeven_sort()

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

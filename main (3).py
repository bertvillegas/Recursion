def digit_sum(n):
  #"""Returns the sum of the digits in the number n.
  #   n is assumed to be an integer."""
  if n==0:
    return 0
  else:
    last_digit = n%10
    return last_digit + digit_sum(n//10)

print(digit_sum(1))

def list_max(lst):
  #"""Returns the max of all elements in lst"""
  if len(lst) == 0:
    return None
  if len(lst) == 1:
   return lst[0]
  max_value = list_max(lst[1:])
  if(max_value > lst[0]):
    return max_value
  else:
    return lst[0]

print(list_max([2,33,26]))

def staircase_paths(stair_count):
  #"""Returns the number of distinct ways someone could climb
     #stair_count stairs, by taking vairous combinations of 1
     #stair steps and 2 stair steps."""
  if (stair_count) <= 1:
    return 1
  single_step = staircase_paths((stair_count)-1)
  double_step = staircase_paths((stair_count)-2)
  return single_step + double_step

#test
#print(staircase_paths(4))
# 43min 27s

# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

def divisible_by(numbers, divisor):
    output=[itemnum for itemnum in numbers if divisible(itemnum, divisor)]
    return output



def divisible(itemnum, divisor):
   
   result=itemnum/divisor
   if not (result).is_integer():

    return False
   else:
    return True




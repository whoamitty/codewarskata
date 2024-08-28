# 43min 27s

# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

# def divisible_by(numbers, divisor):
#     output=[itemnum for itemnum in numbers if (numbers/divisor)%divisor ]
#     return output





def divisible_by(numbers, divisor):
    output=[itemnum for itemnum in numbers if  itemnum%divisor==0 ]
    #output=[itemnum for itemnum in numbers if not itemnum%divisor ] #work too

    print(output)
    return output


divisible_by([1, 2, 3, 4, 5, 6], 2)


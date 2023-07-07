# need function that checks if number is a prime factor of 3 & 5
# if you continue dividing by 3 or 5, you should get to

def _checkNum(num,base1,base2):
  # check for remainders on base1, if good continue

  while num % base1 == 0:
    # print(num)
    num /= base1
  while num % base2 == 0:
    # print(num)
    num /= base2
  if num != 1:
    return False
  else:
    return True
  # check for remainders on base2, if good continue

def check_range(low, high):
  res = []
  for num in range(low,high):
    # print(num)
    if _checkNum(num, 3, 5):
      res.append(num)
  return res

print(check_range(100000,300000))

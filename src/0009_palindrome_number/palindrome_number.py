
def isPalindrome(x: int) -> bool:
  if (x < 0):
    return False
  number = []
  while (x != 0):
    x, digit = divmod(x, 10)
    number.append(digit)
  number_len = len(number) - 1
  for ix in range(0, (number_len + 1) >> 1):
    if number[ix] != number[number_len - ix]:
      return False
  return True

def isPalindrome_2(x: int) -> bool:
  num = str(x)
  return num == num[::-1]

if __name__ == '__main__':
  assert isPalindrome(0)
  assert isPalindrome(5)
  assert not isPalindrome(-5)

  assert isPalindrome(11)
  assert not isPalindrome(12)

  assert isPalindrome(121)
  assert not isPalindrome(123)

  assert isPalindrome(1221)
  assert not isPalindrome(3303)
  assert not isPalindrome(3033)

  assert isPalindrome(1234554321)
  assert not isPalindrome(1234555321)

  assert isPalindrome(12345654321)
  assert not isPalindrome(1234564321)

  print('passed')
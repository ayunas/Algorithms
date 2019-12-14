def fibonacci(n,indent):
  space = ''
  for s in range(indent):
    space = space + ' '

  if n > 0:
    print(space + 'fibonacci(' + str(n) + ')')
  else:
    print(space + 'fibonacci(' + str(n) + ')')

  if n <= 1:
    return 1
  
  return fibonacci(n-1,indent+4) + fibonacci(n-2, indent+8)


print(fibonacci(20,0))


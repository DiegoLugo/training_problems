def fibonacciSequence(iterations: int):
  if iterations <= 1:
    return iterations
  return  fibonacciSequence(iterations - 2) + fibonacciSequence(iterations - 1)

if __name__ == '__main__':
  print(fibonacciSequence(3))
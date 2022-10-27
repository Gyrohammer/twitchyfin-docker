def main():
    
    def factorial(num):
      call_stack = []
      if num == 1:
          print('base case reached! Num is 1.')
          return 1
      else:
       call_stack.append({'input': num})
       print(type(call_stack))
       print('call stack: ', call_stack)
       return num * factorial(num-1)

    factorial(5)



if __name__ == '__main__':
    main()

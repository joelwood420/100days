def fizzbuzz(n=30):
    for i in range(1,n):
        output =''
        if i % 3 == 0: output += 'fizz'
        if i % 5 == 0: output += 'buzz'
        print(output or i)

fizzbuzz(100)



# create a varible for the output, then if it is a multiplte of 3 it will be output plus fizz
# it will then check the second condition and if it is a m ultiple of 5 it will take the current output 
#and concatanate buzz to the output 

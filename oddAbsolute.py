def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")

    result = abs(21 - int(in_num))

    if(int(in_num) > 21):
        result = result*2

    print("Result:",result)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateAbsolute()
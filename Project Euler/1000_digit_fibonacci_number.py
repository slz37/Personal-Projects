#Fibonacci Function
def fibonacci(fnp, fnpp):
    return fnp + fnpp

#Initial
fnp = 1
fnpp = 1
fn = fibonacci(fnp, fnpp)
index = 3

#Run Until 1000 Digits
while len(str(fn)) < 1000:
    #Next Fibonacci Number
    fnpp = fnp
    fnp = fn
    fn = fibonacci(fnp, fnpp)
    index += 1

#Output
print (index)

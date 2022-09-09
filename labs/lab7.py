# lab exercise: circuits in Python 

# Study the comments and code provided,
# before doing the exercises.


# Logic gates; should only be applied
# to "bits", i.e., either 0 and 1
def gnot(x):
    assert x in [0,1]
    return int(not(x)) 
def gand(x,y):
    assert x in [0,1] and y in [0,1]
    return x and y
def gor(x,y):
    assert x in [0,1] and y in [0,1]
    return x or y


# Example: XOR
# Definition x y | x xor y
#            0 0 | 0
#            0 1 | 1
#            1 0 | 1
#            1 1 | 0
# Here is an expression for the 1-rows, using ! for not
#   !xy + x!y 
# Here is code using only the logic gate functions:
def XOR(x,y):
    return gor( gand(gnot(x),y), gand(x,gnot(y)) )

def testXOR():
    assert XOR(0,0) == 0
    assert XOR(0,1) == 1
    assert XOR(1,0) == 1
    assert XOR(1,1) == 0
    print("testXOR success")


# EXERCISE
# Define this function as a single return using
# only the logic gate functions.
def gor3(x,y,z):
    '''Or of three inputs.'''
    return gor(gand(gnot(x),gor(XOR(y,z),gand(y,z))),gand(x,gor(gor(gand(gnot(y),gnot(z)),gand(y,z)),XOR(y,z))))
    '''returns the boolean equation: !x!yz + !xy!z + !xyz +x!y!z + x!yz + xy!z + xyz'''
#Full adder.  See Lecture 6 slide 10
# Implement this as a single return, using only
# the logical gate functions. 
# You may also use gor3 or similar helper functions
# that you write using just gates.
# And you may use assigned-once variables:
# think of those as named wires.

def FA(x,y,cin):
    '''Assume x, y, and cin are bits.
    Return the pair of bits (carry_out,sum) such that
    sum is the low bit of x+y+cin and carry_out is
    the high bit of x+y+carry_in.'''
    carry_out = gor(gor(gand(gand(gnot(x),y),cin),gand(gand(x,gnot(y)),cin)),gor(gand(gand(x,y),gnot(cin)),gand(gand(x,y),cin)))
    '''defines carry_out which is the boolean equation: !xycin + x!ycin + xy!cin +xycin'''
    FAsum = gor(gor(gand(gand(gnot(x),gnot(y)),cin),gand(gand(gnot(x),y),gnot(cin))),gor(gand(gand(x,gnot(y)),gnot(cin)),gand(gand(x,y),cin)))
    '''defines FAsum which equals to boolean equation for sum: !x!ycin + !xy!cin + x!y!cin + xycin'''
    return (carry_out,FAsum)
    '''returns the tuple contain carry_out and the final sum of full adder'''

            
def FAtest(x,y,c):
    '''Compute FA using integer arithmetic.'''
    s = (x+y+c) % 2
    d = 1 if x+y+c >= 2 else 0
    return (d,s)

def testFA():
    assert FA(0,0,0) == FAtest(0,0,0) 
    assert FA(0,1,0) == FAtest(0,1,0) 
    assert FA(1,1,1) == FAtest(1,1,1)
    print("testFA successful on 3 out of 8 cases")


# Review slide 12 of Lecture 6 ("A Circuit for Adding") before continuing.

def twoBitAdd(xx,yy):
    '''Assume xx and yy are pairs (xt,xo) and (yt,yo) of bits.
    Return (cout,(zt,zo)) where (zt,zo) is their two-bit sum
    is the carry bit. Note: xo is the one's place and xt is
    the two's place.  ALERT: use the notation xx[0] to refer to xt,
    and xx[1] to refer to xo.'''
    (c,zo) = FA(xx[1],yy[1],0)
    (d,zt) = FA(xx[0],yy[0],c)
    return (d,(zt,zo))
# Notice the assignments to two variables at once,
# which only works if the right-hand side evaluates to a pair.


def test_twoBitAdd():
    zero = (0,0)
    one = (0,1)
    two = (1,0)
    three = (1,1)
    c,ww = twoBitAdd(one,zero)
    assert( ww == (0,1) and c == 0 )
    c,ww = twoBitAdd(one,one)
    assert( ww == (1,0) and c == 0 )
    c,ww = twoBitAdd(three,three)
    assert( ww == (1,0) and c == 1 )
    print("test_twoBitAdd worked (but incomplete test)")


# EXERCISE: implement the following, using gates and/or FA.
# Hint: you might start by defining something like twoBitAdd
# but that also has a carry input.

def fourBitAdd(xxxx,yyyy):
    '''Assume xxxx is a quadruple (xe,xf,xt,xo) of four bits,
    with xe the high-order bit (i.e., eight's place).  Likewise
    yyyy.  Return (c,zzzz) where zzzz is their four-bit sum
    and c is the carry.'''
    (c,zo) = FA(xxxx[3],yyyy[3],0)
    '''equates the tuple of a carry and sum to the full adder of the last elements of xxxx and yyyy and the carry in of 0'''
    (d,zt) = FA(xxxx[2],yyyy[2],c)
    '''equates the tuple of a carry and sum to the full adder of the second to last elements of xxxx and yyyy and the previous carry out'''
    (e,zy) = FA(xxxx[1],yyyy[1],d)
    '''equates the tuple of a carry and sum to the full adder of the second elements of xxxx and yyyy and the previous carry out'''
    (f,zg) = FA(xxxx[0],yyyy[0],e)
    '''equates the tuple of a carry and sum to the full adder of the first elements of xxxx and yyyy and the previous carry out'''
    return (f,(zg,zy,zt,zo))
    '''returns the final carry out and the altogether sum given by the fourBitAdd computation'''

# EXERCISE: implement the following.
def test_fourBitAdd():
    a = (0,0,0,0)
    b = (1,1,1,1)
    c = (0,0,0,1)
    d = (1,0,0,1)
    f,bbbb = fourBitAdd(a,b)
    assert (f == 0 and bbbb == (1,1,1,1))
    f,bbbb = fourBitAdd(b,c)
    assert (f == 1 and bbbb == (0,0,0,0))
    f,bbbb = fourBitAdd(c,d)
    assert (f == 0 and bbbb == (1,0,1,0))
    f,bbbb = fourBitAdd(a,d)
    assert (f == 0 and bbbb == (1,0,0,1))
    print("test_fourBitAdd worked; more tests plz :/")
    

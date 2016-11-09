############################################################################
# TREVOR ROSS & LUIS PEREIRA
# CS 3600 - Intro to Comp Security
# Project 1
# 10/5/16
############################################################################

def euclid(a, b):
    """
    PURPOSE: recursively calculate the greatest common denominator of a and b
             using the Euclidean Algorithm
    PARAMETERS: a: integer: a > b >= 0
                b: integer: a > b >= 0
    RETURNS: integer, GCD of a and b
    """
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def extended_euclid(a, b):
    """
    PURPOSE: calculates gcd and linear combo of a and b using extended euclidean algorithm
    PARAMETERS: a: integer: a > b >= 0
                b: integer: a > b >= 0
    RETURNS: gcd: integer: greatest common denominator of a, b
             c: integer: from the equation: gcd =  c * a + d * b
             d: integer: from the equation: gcd =  c * a + d * b
    """
    if b == 0:
        # since b == 0, gcd = 1 * a + 0 * 0
        return (a, 1, 0)

    else:
        gcd, c, d = extended_euclid(b, a % b)
        new_c = d # new_c is the old d
        new_d = (gcd - new_c * a) / b # gcd =  c * a + d * b

        return (gcd, new_c, new_d)


def algo_shell():
    """
    PURPOSE: gets a, b from user to feed into GCD(a, b) and linear_comb(a, b)
    """
    ### Reads a and b from text file, which the users input the filename containin a and b ###
    a = int
    b = int
    prog_trace_file = 'gcd.txt'
    #w_file = 'write_file.txt'
    with open(prog_trace_file, 'r') as fhan:
        prog_trace = fhan.readlines()
        print (prog_trace)



    # f = open('gcd.txt', 'r')
    # print f.read()


    a = int(input("Enter an integer value for a: "))
    # ensure a >= 0
    while a < 0:
        a = int(input("Enter an integer value for a: "))

    b = int(input("Enter an integer value for b: "))
    # ensure b >= 0
    while b < 0:
        b = int(input("Enter an integer value for b: "))

    # ensure a >= b
    if b > a:
        temp = b
        b = a
        a = temp

    """ Writing the answer to the external text file called wfile.txt """
    """ It updates everytime a new number is entered. It overwrites previous calculation """


    line1 = "The GCD of %d and %d is: %d" % (a, b, euclid(a, b))
    w_file = raw_input("Enter the name of the output file to store the results: ")
    wfile = open(w_file,'w')
    wfile.write(line1)

    gcd, c, d = extended_euclid(a, b)
    line2 = "\nThe linear combination of GCD(%d, %d) is: %d = (%d) * %d + (%d) * %d" % (a, b, gcd, c, a, d, b)
    wfile.write(line2)

######################### FOR TESTING PURPOSES ONLY ##############################################
import random
import sys
import fractions
def test(num_tests):
    """
    PURPOSE: run tests on euclid() and extended_euclid() by generatating random a and b
    PARAMETERS: num_tests: integer, number of tests to run
    RETURNS: string, either "ERROR..." or "TESTS SUCCESSFUL"
    """
    random.seed()

    # pre-defined tests:
    a, b = 0, 0
    print "TESTING: a = %d, b = %d" % (a, b)
    e_gcd = euclid(a, b)
    if fractions.gcd(a, b) != e_gcd:
        return "ERROR: GCD(%d, %d) = %d is incorrect" % (a, b, e_gcd)
    ee_gcd, c, d = extended_euclid(a, b)
    if e_gcd != ee_gcd:
        return "ERROR: euclid() doesn't agree with extended_euclid(): %d != %d" % (e_gcd, ee_gcd)
    if ee_gcd != a * c + b * d:
        return "ERROR: %d != %d * %d + %d * %d" % (ee_gcd, a, c, b, d)

    # randomly generated tests
    for i in xrange(num_tests):
        a = random.randrange(0, sys.maxint)
        b = random.randrange(0, sys.maxint)
        # ensure a >= b
        if b > a:
            temp = b
            b = a
            a = temp

        print "TESTING: a = %d, b = %d" % (a, b)
        gcd1 = euclid(a, b)
        if fractions.gcd(a, b) != gcd1:
            return "ERROR: GCD(%d, %d) = %d is incorrect" % (a, b, gcd1)
        gcd, c, d = extended_euclid(a, b)
        if gcd1 != gcd:
            return "ERROR: euclid() doesn't agree with extended_euclid(): %d != %d" % (gcd1, gcd)
        if gcd != a * c + b * d:
            return "ERROR: %d != %d * %d + %d * %d" % (gcd, a, c, b, d)

    return "TESTS SUCCESSFUL"
#########################  END FOR TESTING PURPOSES ONLY ##########################################


algo_shell()
# print test(100) # Uncomment to run tests

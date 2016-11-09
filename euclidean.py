############################################################################
# TREVOR ROSS & LUIS PEREIRA
# CS 3600 - Intro to Comp Security
# Project 2
# 11/9/16
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


def get_user_input():
    """ gets the input and output file names from user, returns: (a, b, output_file) """

    in_file = raw_input("Enter the name of the input file that contains a and b: ")
    try:
        with open(in_file, "r") as in_f:
            lines = in_f.readlines()
            a = int(lines[0])
            if a < 0:
                raise ValueError("a = %d but should be >= 0" % a)
            b = int(lines[1])
            if b < 0:
                raise ValueError("b = %d but should be >= 0" % b)
            # ensure a >= b
            if a < b:
                temp = b
                b = a
                a = temp
    except IOError:
        print "Invalid input file. Try using 'input.txt'."
        exit(1)
    except ValueError:
        print "Invalid data format type in", in_file
        print "CORRECT FORMAT: line 1: a (int), line 2: b (int)"
        print "FILE CONTENTS:"
        for line in lines:
            print line,
        exit(1)

    out_file = raw_input("Enter the name of the output file to store the GCD of a and b,\
    and the linear combination of GCD(a, b): ")

    return (a, b, out_file)


def main():
    """
    PURPOSE: gets a, b from user to feed into GCD(a, b) and linear_comb(a, b)
    """
    # Writing the answer to the external text file called wfile.txt
    # It updates everytime a new number is entered. It overwrites previous calculation

    # get input from files/user
    a, b, out_file = get_user_input()
    # find gcd, linear equation
    line1 = "The GCD of %d and %d is: %d\n" % (a, b, euclid(a, b))
    gcd, coef_a, coef_b = extended_euclid(a, b)
    line2 = "Coefficient of a: %d\n" % coef_a
    line3 = "Coefficient of b: %d\n" % coef_b
    # write results to file
    with open(out_file,'w') as wfile:
        wfile.write(line1)
        wfile.write(line2)
        wfile.write(line3)
    print "FINISHED"


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

if __name__ == "__main__":
    main()
    # print test(100) # Uncomment to run tests

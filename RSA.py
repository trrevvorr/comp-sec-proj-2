############################################################################
# TREVOR ROSS & LUIS PEREIRA
# CS 3600 - Intro to Comp Security
# Project 3
# 10/16/16
############################################################################

def extended_euclid(a, b):
    """
    PURPOSE: calculates gcd and linear combo of a and b using extended euclidean algorithm
    PARAMETERS: a: integer: a > b >= 0
                b: integer: a > b >= 0
    RETURNS: gcd: integer: greatest common denominator of a, b
             c: integer: from the equation: gcd =  c * a + d * b
             d: integer: from the equation: gcd =  c * a + d * b
    """
    # ensure a >= b
    if a < b:
        temp = b
        b = a
        a = temp

    if b == 0:
        # since b == 0, gcd = 1 * a + 0 * 0
        return (a, 1, 0)

    else:
        gcd, c, d = extended_euclid(b, a % b)
        new_c = d # new_c is the old d
        new_d = (gcd - new_c * a) / b # gcd =  c * a + d * b

        return (gcd, new_c, new_d)


def encrypt(x, e, n):
    """ encrypt x using e and n """
    return (x ** e) % n


def decrypt(c, d, n):
    """ decrypt c using d and n """
    return (c ** d) % n


def main():
    """
    PURPOSE: gets a, b from user to feed into GCD(a, b) and linear_comb(a, b)
    """
    # get file contating p, q, and e
    in_file = raw_input("\nEnter the name of the file that contains p, q and e: ")
    with open(in_file, "r") as in_f:
        lines = in_f.readlines()
        p = int(lines[0])
        q = int(lines[1])
        e = int(lines[2])

    # calculate n and o(n) (num_rel_primes)
    n = p * q
    num_rel_primes = (p - 1) * (q - 1)

    # find the private key d
    gcd, coef_a, coef_b = extended_euclid(num_rel_primes, e)
    if gcd != 1:
        raise ValueError("GCD must = 1 in order for multiplicitive inverse to exist")
    d = coef_b
    while d < 0:
        # make d positive
        d += num_rel_primes
    print "p: %d, q: %d, n: %d, e: %d, o(n): %d, d: %d" % (p, q, n, e, num_rel_primes, d) # REMOVE

    # write N, e, and d to output file
    out_file = raw_input("\nEnter the name of the output file to store d and N: ")
    with open(out_file, "w") as key_file:
        key_file.write("Public key (N, e): (%d, %d)\n" % (n, e))
        key_file.write("Private key d: %d" % d)

    # get x, number to be encrypted
    x_file = raw_input("\nEnter the name of the file that contains x to be encrypted using (N, e): ")
    with open(x_file, "r") as fhan:
        x = int(fhan.readline())
    print "Read in x as:", x # REMOVE
    if x >= n:
        raise ValueError("x (%d) must be less than N(%d)" % (x, n))

    # encrypt c, write to file
    c = encrypt(x, e, n)
    c_file = raw_input("\nEnter the output file name to store E(x): ")
    with open(c_file, "w") as fhan:
        fhan.write(str(c))
    print "Encrypted x to c:", c # REMOVE

    # get c, decrypt using d
    c_file = raw_input("\nEnter the name of the file that contains c to be decrypted using d: ")
    with open(c_file, "r") as fhan:
        c = int(fhan.readline())
    print "Read in c as:", c # REMOVE

    # decrypt c, write to file
    decrypted_c = decrypt(c, d, n)
    decrypted_file = raw_input("\nEnter the output file name to store D(c): ")
    with open(decrypted_file, "w") as fhan:
        fhan.write(str(decrypted_c))
    print "Decrypted c to:", decrypted_c # REMOVE

    if x == decrypted_c:
        print "SUCCESSFULL ENCRYPTION AND DECRYPTION"
    else:
        print "ERROR: x = %d, decrypted c = %d" % (x, decrypted_c)

if __name__ == "__main__":
    main()


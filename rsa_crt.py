import math
import sys
sys.float_info.max
import decimal
from decimal import Decimal, getcontext
decimal.getcontext().prec = 1000000
import time

def chinese_remainder_theorem(c, d, p, q):
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = modinv(q, p)  #calculates the inverse
    m1 = pow(c % p, dp, p)
    m2 = pow(c % q, dq, q)
    h = q_inv * (m1 - m2) % p
    m = m2 + h * q
    return m

def modinv(e, phi): #function used to calculate modular inverse
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:  #extended euclidean algorithm
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def gcd(a, h): #function used to calculate the GCD
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

start_time = time.time()

#p and q are 1024 bit primes. Tested using Miller Rabbin algorithm from Question 2
p = decimal.Decimal(93157514440008416060152581209771328084315540744108777247282877742642144228996436767301076617459132669720250344435067486384372831297864177679930280542953705820550841452643298642479650081541144705769192320864930023229624400115786136825259699527269970156914780682920747497892608805592718576071533419891979467457)
q = decimal.Decimal(114700298000536603768250623889386148869193563125296495088456294960151865069691038180525157058394432935782417899944021692062697489611470240931049725771829277569181543554099090839974654830294909991149412096851361848408763186105321155157830728196048959026745794847487774577017451227169959359497085179742256260153)
n = decimal.Decimal(0)
n = p*q
e = 65537
phi = decimal.Decimal(0)
phi = (p-1)*(q-1)
d = decimal.Decimal(0)
d = modinv(e, phi)

msg = decimal.Decimal(476921883457909)

print("Message data = ", msg)

c = decimal.Decimal(0)
c = pow(msg, e, n) #encryption c = (msg ^ e) % n
print("Encrypted data = ", c)

decrypted_msg = chinese_remainder_theorem(c, d, p, q) #decryption using chinese remainder theorem
print("Original Message Sent = ", decrypted_msg)

end_time = time.time()

elapsed_time = end_time - start_time
print("Time taken for RSA with CRT: {:.6f} seconds".format(elapsed_time))

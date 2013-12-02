#!/usr/bin/env python
#Implementing the Homomorphic Encryption with Integer!!!!!
#Programmed By : Aruj Parajuli(arujparajuli@gmail.com)
import random

#Defining the Key Module
def keygen(noise, modulus=2):
    a_key = random.getrandbits((noise ** 2))

    while ((a_key % 2) != 1) and (a_key < (modulus ** (noise ** 2) - 1)):
        a_key = a_key + 1

    return a_key

#Defining the Encryption Mechanism
def encrypt(noise, a_key, a_bit, modulus=2):
    a_mask          = random.getrandbits(noise)
    a_bit_remainder = a_bit % modulus

    while ((a_mask % modulus) != a_bit_remainder):
        a_mask = random.getrandbits(noise)

    return a_mask + (a_key * random.getrandbits(noise ** 5))

#Defining the Decryptiong Mechanism
def decrypt(a_key, a_bit, modulus=2):
    return (a_bit % a_key) % modulus


def demo():
    modulus         = 32
    noise           = 6
    a_key           = keygen(noise, modulus=modulus)
    a_random_bit    = random.getrandbits(5)
    a_cipher_bit    = encrypt(noise, a_key, a_random_bit, modulus=modulus)
    a_decrypted_bit = decrypt(a_key, a_cipher_bit, modulus=modulus)

    print("Simple Exam Demonstrating the Encrption and Decrpytion Behavior\n----------------")
    print("key: %d\nplaintext: %d\ncrpyted:-------- %d\nDecrpyted:-------- %d\n\n" % (a_key, a_random_bit, a_cipher_bit, a_decrypted_bit))

def multiplication():
    modulus = 16
    noise   = 5
    a_key   = keygen(noise, modulus=modulus)
    print("Input the Integer for Multiplication:--------------------------------\n")
    
    a_p = input("Enter the First Integer: ")
    #a_p     = random.getrandbits(2)
    #b_p     = random.getrandbits(2)
    
    b_p = input("Enter the Second Integer: ")
    a_c     = encrypt(noise, a_key, a_p, modulus=modulus)
    b_c     = encrypt(noise, a_key, b_p, modulus=modulus)
    c       = a_c * b_c
    d       = decrypt(a_key, c, modulus=modulus)
    print("Multiplication of Two Number in Encrypted and Decrypted\n-------------------------")
    print("First Integer: %d\nSecond Integer: %d\n" % (a_p, b_p))
    print("Cryptic Format of First Integer: %d\nCryptic Format of First Integer of Second Integer: %d\n" % (a_c, b_c))
    print("Crypto:------- %d\nDecrpyted:-------- %d\n\n" % (c, d))

def addition():
    modulus = 8
    noise   = 4
    a_key   = keygen(noise, modulus=modulus)
    print("Input the Integer for Additon:----------------\n")
    a_p = input("Enter the First Integer: ")
    b_p = input("Enter the Second Integer:")
    a_c     = encrypt(noise, a_key, a_p, modulus=modulus)
    b_c     = encrypt(noise, a_key, b_p, modulus=modulus)
    c       = a_c + b_c
    d       = decrypt(a_key, c, modulus=modulus)
    print("\nAddition of Two Number in Encrypted and Decrypted Format:\n------------------")
    print("First Integer: %d\nSecond Integer: %d\n" % (a_p, b_p))
    print("Cryptic Format of First Integer: %d\nCryptic Format of First Integer of Second Integer: %d\n" % (a_c, b_c))
    print("Crypto:------- %d\nDecrpyted:-------- %d\n\n" % (c, d))
    

demo()
multiplication()
addition()

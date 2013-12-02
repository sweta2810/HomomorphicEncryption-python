HomomorphicEncryption-python
============================

It kind of encryption mechanism mostly used in cloud which allows specific types of computations to be carried out on ciphertext and obtain an encrypted result which decrypted matches the result of operations performed on the plaintext.


Introduction
============================



Sice after the years research of [Homomorphic Encryption](http://en.wikipedia.org/wiki/Homomorphic_encryption) Web user would send encrypted data to a server in the cloud, which would process it without decrypting it and send back a still-encrypted result.Previous we have to take risk about storing our data in cloud provider like: Google, Dropbox but in server side we can implement these feature then hell no one can touch you.
In Homomorphic Encryption we try to implement basic concept to encrypt the data before sending them to the Cloud provider. But, this one will have to decrypt them each time he has to work on them. The client will need to provide the private key to the server to decrypt the data before execute the calculations required, which might affect the confidentiality of data stored in the Cloud.The Homomorphic Encryption method is able to perform operations of encrypted data without decrypting them.
For Further Reseach Paper and Computation :[Homomorphic Encryption](http://www.iaeng.org/publication/WCE2012/WCE2012_pp536-539.pdf)


Implementation
============================
In the package we try to implement simple homomorphic encryption in python in only for the case of integer and soon more yet come interacting with openstack in localmachine...




>>To run python homo.py
Enter the desired integer input to see the result with the output of crypted and decrypted text


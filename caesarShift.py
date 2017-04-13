def encrypt(plaintext, shift):
	cyphertext = ''
	for letter in plaintext:
		letter = chr(ord(letter) + shift)
		cyphertext += letter
	return cyphertext

def decrypt(cyphertext, shift):
	plaintext = ''
	for letter in cyphertext:
		letter = chr(ord(letter) - shift)
		plaintext += letter
	return plaintext

msg = raw_input("Enter some text to encrypt: ")
shift = int(raw_input("Enter the desired shift: "))

print "Your message:", msg
print "Encrypted:", encrypt(msg, shift)
print "Decrypted:", decrypt(encrypt(msg,shift), shift)
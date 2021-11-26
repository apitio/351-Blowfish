from flask import Flask, request, render_template
import blowfish
from os import urandom

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/result', methods = ['POST', 'GET'])
def my_form_post():

    #Fetch plaintext and key from form.html submitted form  
    plaintext = request.form['plaintext']
    key = request.form['key']

    #Convert form values into binary values to encrypt the characters
    key_binary = key.encode('ascii')
    plaintext_binary = plaintext.encode('ascii')

    #Call the blowfish cipher method from the imported blowfish function
    cipher = blowfish.Cipher(key_binary)

    # initialization vector by using random from OS
    iv = urandom(8) 

    #Encrypt the plaintext using OFB method and IV
    data_encrypted = b"".join(cipher.encrypt_ofb(plaintext_binary, iv))

    #Decrypt the ciphertext using OFB method and IV
    data_decrypted = b"".join(cipher.decrypt_ofb(data_encrypted, iv))

    #Write the encrypted binary data to encrypted.dat file
    fout = open('encrypted.dat', 'wb')
    fout.write(data_encrypted)
    fout.close()

    #Write the decrypted binary data to decrypted.dat file
    fout = open('decrypted.dat', 'wb')
    fout.write(data_decrypted)
    fout.close()

    #Return if no errors
    return "Encrypted Succesfully!"



if __name__ == '__main__':
   app.run()

from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VignenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCypher
app = Flask(__name__)

#caesar cipher

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key= int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key= int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
#Vigenere
vigenere_cipher = VignenereCipher()

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key= data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key= data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'decrypted_text': decrypted_text})
#Railfence

railfence_cihper = RailFenceCipher()
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key= int(data['key'])
    encrypted_text = railfence_cihper.rail_fence_encypt(plain_text,key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key= int(data['key'])
    decrypted_text = railfence_cihper.rail_fence_decrypt(cipher_text,key)
    return jsonify({'decrypted_text': decrypted_text})
#plaifair
playfair_cypher=PlayFairCypher()
@app.route('/api/playfair/cratematrix',methods=['POST'])
def playfair_creatematrix():
    data=request.json
    key = data['key']
    playfair_matrix = playfair_cypher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix":playfair_matrix})
@app.route('/api/playfair/encrypt',methods=["POST"])
def playfair_encrypt():
    data= request.json
    plain_text= data['plain_text']
    key=data['key']
    playfair_matrix = playfair_cypher.create_playfair_matrix(key)
    encrypted_text= playfair_cypher.playfair_encrypt(plain_text,playfair_matrix)
    return jsonify({'enypetd_text':encrypted_text})
@app.route('/api/playfair/decrypt',methods=["POST"])
def playfair_decrypt():
    data= request.json
    cipher_text= data['cipher_text']
    key=data['key']
    playfair_matrix = playfair_cypher.create_playfair_matrix(key)
    decrypted_text= playfair_cypher.playfair_decrypt(cipher_text,playfair_matrix)
    return jsonify({'deypetd_text':decrypted_text})
#main
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
import argparse

parser = argparse.ArgumentParser(prog='Cesar Cipher Encrypt/Decrypt', description='You can encrypt and decrypt your text.')

parser.add_argument('-m', '--method', required=True, help="decrypt or encrypt")
parser.add_argument('-t', '--text', required=True, nargs='+', help="Your plain text")
parser.add_argument('-n', '--number', required=False, help="Shift number")
parser.add_argument('-w', '--wordlist', required=False, help="Bruteforce wordlist")

args = parser.parse_args()
alp = ["a","b","c","d","e","f",
       "g","h","i","j","k","l",
       "m","n","o","p","q","r",
       "s","t","u","v","w","x",
       "y","z"]

metod = args.method


def encrypt(word, ciph_no):
    crypt_word = ""
    for w in word:
        is_upper = False
        w = str(w)
        if not w.lower() in alp:
            crypt_word = crypt_word + str(w)
        else:
            ind = alp.index(w.lower())
            new_ind = ind + ciph_no
            if w.upper() == w:
                is_upper = True
            if new_ind >= len(alp):
                new_ind = new_ind % len(alp)
            if not is_upper:
                crypt_word = crypt_word + str(alp[new_ind])
            else:
                crypt_word = crypt_word + str(alp[new_ind]).upper()
    return crypt_word


if metod == "encrypt":
    words = args.text
    cip_no = args.number
    encrypted_words = []
    for word in words:
        encrypted_words.append(encrypt(word=word, ciph_no=int(cip_no)))
    print("Encrypted: " + " ".join(encrypted_words))
elif metod == "decrypt":
    enc_words = args.text
    word_file = args.wordlist
    flag = False
    found = ""
    enc_words = " ".join(enc_words)
    for i in range(len(alp)):
        with open(word_file, "r") as w_f:
            for ww in w_f.readlines():
                test_enc = encrypt(ww, i)
                
                if test_enc.strip() == enc_words.strip():
                    flag = True
                    found = ww
                    break
        w_f.close()
        if flag:
            break

    if flag:
        print("Found: " + found)
    else:
        print("No found")
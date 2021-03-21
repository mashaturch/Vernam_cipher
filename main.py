"""Шифр Вернама (одноразовый блокнот) - единственный известный абсолютно секретный шифр. Он основан на том,
что сообщение кодируется побитовым кодом с одноразовым ключом, длина которого не меньше длины передаваемого сообщения.

Условие задачи:

Сначала программа просит, чтобы пользователь ввёл текст, который он хочет зашифровать или расшифровать.
Затем у пользователя спрашивают 3 вопроса:

1) Хочет он только зашифровать сообщение (да или нет)?
2) Хочет он зашифровать это сообщение и потом вернут исходный текст, то есть расшифровать этот зашифрованный текст?
3) Хочет только рашифровать текст? Если выбрал 3 пункт, то просит ещё ввести ключи расшифровки.

Если никакой из вариантов не выбран, то просит ввести занового данные.

После выбранного варианта пользователю выводится для каждого из пунктов:
1) зашифрованный текст и ключи шифрования
2) зашифрованный текст, ключи шифрования и расшифрованный текст
3) расшифрованный текст

"""

"""Vernam encryption and decryption"""

from random import randint

def encryption (text):
    """Encrypting the message"""
    keys = ''
    text_encryption = ''
    for char in text:
        key = randint (0, 25)
        keys = keys + str (key) + ' '
        if 'A' <= char <= 'Z':
            save = ord (char) + key - 13
            text_encryption += chr ((save % 26) + ord ('A'))
        else:
            text_encryption += ' '

    data = text_encryption + '/' + keys + '/' + str (save)
    print ('Encrypted message:', text_encryption)
    print ('Keys of program:', keys)
    return data

def list_keys (keys):
    """Creating a list with keys"""
    list = []
    key = ''
    for i in range (len (keys)):
        if keys[i] == ' ':
            list.append (key)
            key = ''
        else:
            key += keys[i]
    return list

def decryption (text_encryption_out, keys_out, save):
    """Message decryption for encrypting the message before"""
    list_key = list_keys(keys_out)
    decrypt = ''
    save = int (save)
    for i,j in enumerate (text_encryption_out):
        if 'A' <= j <= 'Z':
            save = ord (j) - int (list_key[i]) - 13
            decrypt += chr ((save % 26) + ord ('A'))
        else:
            decrypt += ' '
    print (decrypt.capitalize())

def decryption_input (text, keys):
    """Decryption of the entered text"""
    text_out = ''
    keys = keys.split ()
    for i, char in enumerate (text):
        if char == ' ':
            text_out += ' '
            continue
        elif keys[i] != '':
            text_out += chr((ord(char) - int (keys[i]) - 13) % 26 + ord('A'))
    print (text_out.capitalize())

def main ():
    """Main program execution"""
    text = input('Enter the message you want to encrypt: ')
    text = text.upper()
    question = input ('Do you only want to encrypt the text? ')
    if question.lower() == 'yes':
        encryption_out = encryption(text)
    else:
        question_2 = input ('Do you want to encrypt the text and show its decryption after running the whole program? ')
        if question_2.lower() == 'yes':
            encryption_out = encryption (text)
            text_encryption_out, keys_out, save = encryption_out.split ('/')
            decryption(text_encryption_out, keys_out, save)
        else:
            question_3 = input('Do you only want to decrypt the text? ')
            if question_3.lower() == 'yes':
                keys = input ('Enter encryption keys: ')
                decryption_input(text, keys)

            else:
                print ('There is nothing we can do, please answer the question again!')
                main ()

# Start program
main ()
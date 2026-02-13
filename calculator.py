def toplama(num1, num2):
    return num1 + num2

def eksilt(num1, num2):
    return num1 - num2

def bol(num1, num2):
    return num1 / num2

def carp(num1, num2):
    return num1 * num2


while(True):
    islem = str(input("""
                Yapmak istediğiniz işlemi seçin:
                      toplama   1
                      çıkarma   2
                      bölme     3
                      çarpma    4
                      çıkmak için q basın...
            """))
    

    num1 = int(input("Birinci sayıyı girin: "))
    num2 = int(input("İkinci sayıyı girin: "))

    if(islem == '1'):
        result = toplama(num1, num2)
    elif(islem == '2'):
        result = eksilt(num1, num2)
    elif(islem == '3'):
        result = bol(num1, num2)
    elif(islem == '4'):
        result = carp(num1, num2)
    elif(islem == 'q'):
        break
    else:
        print("Yanlış bir giriş yaptınız.")

    print(f"Yaptığınız işlemin sonucu {result}")

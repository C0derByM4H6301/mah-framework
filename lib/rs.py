import random
from colorama import *
init(autoreset=True)
class random_sentence:
    def random_sent():
        num = random.randrange(1,9)
        def sentence1():
            #print("bünyamin")
            sentence1="Öğüt vermek kolay , Örnek olmak zordur..."
            sentence1_eng="It's easy to give advice, it's hard to be an example."
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence1)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence1_eng)
        def sentence2():
            #print("ahmet")
            sentence2="Hayat olmus yaşam maşam surileri sikim sabah akşam"
            sentence2_eng="I couldn't translate this."
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence2)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence2_eng)
        def sentence3():
            # print("anonymous")
            sentence3="Aleksandır indir kaldır ferahlandır!"
            sentence3_eng="I couldn't translate this"
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence3)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence3_eng)
        def sentence4():
            # print("anonymous")
            sentence4="Emin olmak zor..."
            sentence4_eng="Being Emin is hard..."
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence4)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence4_eng)
        def sentence5():
            sentence5="Adım Erkan olmadığından Mahmut'u seviyorum"
            sentence5_eng="I love Mahmut because my name is not Erkan"
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence5)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence5_eng)
        def sentence6():
            sentence6="Bir oyuncunun değer verdiği bir karekter: Kamikaze Xaero"
            sentence6_eng="A character that a player values: Kamikaze Xaero"
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence6)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence6_eng)
        def sentence7():
            sentence7="iki kişi hata yaptı birisi yüzü için sevdi,\n birisi sevmeyeceği bildiği halde sevdi"
            sentence7_eng ="Two people made mistakes, one loved for his face, one loved even though he knew he wouldn't"
            print(Fore.YELLOW+"Turkish:")
            print(Fore.CYAN+sentence7)
            print(Fore.YELLOW+"English:")
            print(Fore.CYAN+sentence7_eng)
        def sentence8():
            sentence8="Süleyman Çakır (d. 1964 - ö. 8 Nisan 2004)"
            print(Fore.YELLOW+"Engilsh: We remember with respect and love...")
            print(Fore.YELLOW+"Saygı ve sevgiyle anıyoruz...")
            print(Fore.BLUE+sentence8)
        if num==1:
            sentence1()
        if num==2:
            sentence2()
        if num==3:
            sentence3()
        if num==4:
            sentence4()
        if num==5:
            sentence5()
        if num==6:
            sentence6()
        if num==7:
            sentence7()
        if num == 8:
            sentence8()
print("西暦世紀変換プログラム©2022 Soy乳")
while True:
    century_input:int=input("求めたい西暦を入力してください")
    century= int(century_input) / 100
    century_remainder=int(century_input)%100
    if century_remainder==0 :
        print(int(century),"世紀")
    else:
        print(int(century)+1,"世紀")
    type=input("このまま繰り返す場合はyをプログラムを終了する場合はnを入力してください。")
    if type=="y" :
        pass
    else:
        break
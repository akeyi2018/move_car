#最初は全開するが、惰性で4割まで落とす制御リストを作成する
speedChangeList = [round(speed*0.1, 1) for speed in range(10, 4, -2)]

#for speed in range(10, 4, -2):
#    print(speed)
#for speed in range(10):
#    print(speed)
    
    #作成したリストに従ってコントローする
for listSpeed in speedChangeList:
    print(listSpeed)
    #    test3.StartRoll(listSpeed)
    #    sleep(0.2)
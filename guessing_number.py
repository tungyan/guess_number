import random

def Start_Guess():
    print("现在系统在1-100之间随机生成了一个正整数，而你有6次机会猜对它！\n")
    ranNumber = random.randint(1,100)
    limit = 0
    active = True
    while active:
        userAnswer = input("现在你还有 "+str(6 - limit)+" 次机会喔,快输入你要猜的数吧.\n ")
        try:
            if(int(userAnswer) == ranNumber):
                userResult = input("恭喜你，答对了！再来一局请按'y'，退出游戏请按'q'.\n")
                while (userResult.lower() != 'q' and userResult.lower() != 'y'):
                    userResult = input("请输入'q'或者'y'.\n")
                if(userResult.lower() == 'q'):
                    print("bye！")
                    active = False
                elif(userResult.lower() == 'y'):
                    Start_Guess()
                    break
            elif(int(userAnswer) < ranNumber):
                print("额...你猜的数小了喔\n")
            elif(int(userAnswer) > ranNumber):
                print("额...你猜的数大了喔\n")
        except ValueError:
            print("只可以输入1-100间的正整数喔！\n")
        else:
            limit += 1
            if(limit == 6):
                print("很遗憾...你的6次机会都用完了.正确的数是 " + str(ranNumber))
                active = False

userInput = input("欢迎来玩猜数游戏，按任意键开始，按'q'键退出.\n")
if(userInput.lower() == 'q'):
    print("bye！")
else:
    Start_Guess()



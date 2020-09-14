import time
import random

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————第 {} 局！start！——————'.format(i))
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        print('【你】\n血量：{}\n攻击：{}'.format(player_life,player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：{}\n攻击：{}'.format(enemy_life,enemy_attack))
        print('-----------------------')
        time.sleep(1)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack 
            enemy_life = enemy_life - player_attack
            print('敌人啪叽地打了你一下，【你】剩余血量{}'.format(player_life))
            print('你咚地踹了敌人一下，【敌人】血量剩余{}'.format(enemy_life))
            print('-----------------------')
            time.sleep(1.5)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人狗带了，你赢了！哟呵，小样儿还不错嘛！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('长那么大干什么吃的！连个电脑都打不过！:)')
        else:
            print('平局。。。看我表情:(')

    if player_victory > enemy_victory :
        time.sleep(1)
        print('\n【最终结果：you win!（别告诉我你看不懂英文:)）】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你赢啦~！（你以为我会这么说？当然是你输了啊，呵呵！）】')
    else: 
        print('\n【最终结果：平局。不，等下。你连个计算机都打不过，还是输了算了。所以，you lose！！！】')

    a1 = input('还玩不玩了！不玩lz睡了！（输入n退出，输入其他继续）：')
    if a1 == 'n':
        break


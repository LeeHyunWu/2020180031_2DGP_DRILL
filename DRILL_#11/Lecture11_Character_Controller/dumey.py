# class Star:     # 클래스 역할 : 함수 또는 변수를 그룹 이름으로 묶는 것
#     x = 100
#
#     def change():
#         x = 200
#         print("x is", x)
#
# print(Star.x)   # Star:클래스, x:클래스 변수
# Star.change()
#
# star = Star()   # 객체 생셩용이 아니어도 객체는 만들어진다.
# star.change()
#
#
# class Player:
#     def __init__(ttt):
#         ttt.x = 100
#
#     def where(sss):
#         print(sss.x)
#
# player = Player()
# player.where()
#
# # Player.where()      # 클래스의 함수 호출
# Player.where(player)
# player.where()      # 객체 함수 호출 == Player.where(player)


table = {
    "SLEEP" : {'HIT' : 'WAKE'},
    "WAKE" : {'TIMER10':'SLEEP'}
}
cur_state = 'SLEEP'
event = 'HIT'
next_state = table[cur_state][event]
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])
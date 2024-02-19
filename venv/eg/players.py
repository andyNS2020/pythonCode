# 这是一个示例 Python 脚本。
# 切片、遍历、复制列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(players[:4])
print(players[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())
players2 = players
print(players)
print(players2)
for player in players[0:len(players)]:
 players2.append(player)
players.append('players')
players2.append('players2')
print(players)
print(players2)
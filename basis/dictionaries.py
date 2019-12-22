nba_player={'center':'Yao',
            'sg':  'Kobe',
            'pg': 'AI'}
print(nba_player['center'])
nba_player['sf']='LBJ'
print(nba_player)
del nba_player['sg']
print(nba_player)
nba_player.pop('pg')
print(nba_player)
print(nba_player.popitem())
print(nba_player)
print('sf' in nba_player)
print('center' in nba_player)

b={'center':'Shaq',
            'sg':  'Kobe',
            'pg': 'AI'}

nba_player.update(b)
print(nba_player)
print(nba_player.items())

info=dict.fromkeys([6,7,8], [1,{'name':'michael'},'b'])
print(info)
info[6][1]['name']='iverson'
print(info)

for i in b:
    print(i,b[i])

for k,v in info.items():
    print("sss---",k,v)
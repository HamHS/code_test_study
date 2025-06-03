n,m = map(int,input().split())
map_list = []
count = 1
players_back = None
player_start_position = list(map(int,input().split()))
player_xpos = player_start_position[0]
player_ypos = player_start_position[1]
player_head = player_start_position[2]
for i in range(n):
    map_list.append(list(map(int,input().split())))

map_list[player_xpos][player_ypos] = 2

while True:
    if player_head == 0:
        player_head = 3
        players_back = [player_xpos,player_ypos+1]
        if map_list[player_xpos][player_ypos-1] == 0:
            map_list[player_xpos][player_ypos-1] = 2
            player_ypos -= 1
            count += 1
    elif player_head == 1:
        player_head = 0
        players_back = [player_xpos+1, player_ypos]
        if map_list[player_xpos-1][player_ypos] == 0:
            map_list[player_xpos-1][player_ypos] = 2
            player_xpos -= 1
            count += 1
    elif player_head == 2:
        player_head = 1
        players_back = [player_xpos-1, player_ypos]
        if map_list[player_xpos][player_ypos+1] == 0:
            map_list[player_xpos][player_ypos+1] = 2
            player_ypos += 1
            count += 1
    elif player_head == 3:
        player_head = 2
        players_back = [player_xpos, player_ypos - 1]
        if map_list[player_xpos+1][player_ypos] == 0:
            map_list[player_xpos+1][player_ypos] = 2
            player_xpos += 1
            count += 1

    if (map_list[player_xpos+1][player_ypos] > 0 and map_list[player_xpos][player_ypos+1] > 0
        and map_list[player_xpos-1][player_ypos] > 0 and map_list[player_xpos][player_ypos-1] > 0):
        if map_list[players_back[0]][players_back[1]] == 1:
            break
        else:
            player_xpos = players_back[0]
            player_ypos = players_back[1]
print(count)

def search_Player_ID(FirstName, LastName, Position = None):
    if not Position:
        query = {'api_key':api_key, 'first_name':FirstName, 'last_name':LastName}
    else:
        query = {'api_key':api_key, 'first_name':FirstName, 'last_name':LastName, 'position':Position}
    tmp = requests.post(url_NBA_player, data = query)
    tmp_dict = eval(tmp.content[1:-1])
    return tmp_dict['player_id']

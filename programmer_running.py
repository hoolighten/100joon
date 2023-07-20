def solution(players, callings):
    player_dict = {player: rank for rank, player in enumerate(players)}
    rank_dict = {rank: player for rank, player in enumerate(players)}
    for calling_name in callings:
        rank = player_dict[calling_name]
        rank_dict[rank], rank_dict[rank - 1] = rank_dict[rank - 1], rank_dict[rank]
        player_dict[rank_dict[rank]], player_dict[rank_dict[rank - 1]] = player_dict[rank_dict[rank - 1]], player_dict[
            rank_dict[rank]]
    return list(rank_dict.values())

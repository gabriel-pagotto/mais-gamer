def limit_notices(game_id, notices):
    necessary_notices = []
    for notice in notices:
        if notice.game_id == game_id:
            necessary_notices.append(notice)
    if len(necessary_notices) < 3:
        return None
    if len(necessary_notices) >= 3:
        return [necessary_notices[0], necessary_notices[1], necessary_notices[2]]
    return necessary_notices

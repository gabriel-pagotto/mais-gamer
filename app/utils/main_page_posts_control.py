from app.models import Posts
from app.utils.date_time import get_datetime_7_days

def posts_control():
    posts = Posts.query.all()
    last_notices = []
    for post in posts:
        last_notices.append(post)
    last_notices.reverse()
    last_notice = last_notices[0]
    rest_notices = [
        last_notices[1],
        last_notices[2],
        last_notices[3],
        last_notices[4],
        last_notices[5],
        last_notices[6],
    ]

    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])

    '''top_five_week = []
    notices_to_be_deleted = []
    top_five_counter = 0

    for notice in last_notices:
        print(top_five_counter)
        if get_datetime_7_days(notice.addedAt) == True:
            top_five_week.append(post)
            notices_to_be_deleted.append(top_five_counter)

        top_five_counter = top_five_counter + 1
    
    for number in notices_to_be_deleted:
        del(last_notices[number])'''


    return [
        posts,
        last_notice,
        last_notices,
        rest_notices,   
    ]

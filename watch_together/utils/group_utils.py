from watch_together.models import db, Group, User


def get_content_id_from_video_url(video_url):
    return video_url.strip().split('/')[-1]


def create_group(payload):
    content_id = get_content_id_from_video_url(payload['video_url'])
    group = Group(
        name=payload['group_name'],
        content_id=content_id,
        tenant_id='in'
    )
    data = group.json()
    db.session.add(group)
    # import ipdb
    # ipdb.set_trace()
    x = db.session.commit()
    print x
    # for user in payload['users_email']:
    #     db.session.add(user)
    # db.session.commit()
    return data


def create_user(group_id, user_email):
    """

    :param group_id:
    :param user_email:
    :return:
    """
    user = User(
        group_id=group_id,
        user_email_id=user_email,
        current_run_time=None,
        is_paused=False
    )
    return user


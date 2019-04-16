import uuid

from watch_together.models import db, Group, User


def get_content_id_from_video_url(video_url):
    return video_url.strip().split('/')[-1]


def create_group(payload):
    content_id = get_content_id_from_video_url(payload['video_url'])
    group_id = str(uuid.uuid4())
    group = Group(
        id=group_id,
        name=payload['group_name'],
        content_id=content_id,
        tenant_id='in'
    )
    data = group.json()
    db.session.add(group)
    db.session.commit()
    for email_id in payload['users_email']:
        user = User(
            id=str(uuid.uuid4()),
            group_id=group_id,
            email_id=email_id,
            is_paused=False,
            current_run_time=None
        )
        db.session.add(user)
    db.session.commit()
    return data


def create_user(group_id, user_email):
    """

    :param group_id:
    :param user_email:
    :return:
    """
    user = User(
        id=str(uuid.uuid4()),
        group_id=group_id,
        email_id=user_email,
        current_run_time=None,
        is_paused=False
    )
    return user


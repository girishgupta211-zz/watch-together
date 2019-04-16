import uuid

from watch_together.models import db, Group, User
from watch_together.utils.cms_utils import get_master_manifest


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

    return group_id


def get_group_by_id(group_id):
    """

    :param group_id:
    :return:
    """
    cursor = db.session.query(Group).filter(
        Group.id == group_id
    )

    return cursor


def get_master_manifest_start_time(group_id):
    cursor = get_group_by_id(group_id)
    group = cursor.first()
    if not group:
        raise Exception("group not found")

    group = group.json()
    return get_master_manifest(group['content_id']), group['start_time']


"""
Policies:

                user                            entity
admin           admin=1                         -
owner(wid)      user.wid == entity.wid          world
owner(iso)      user.iso == entity.iso          country, entity, etc
owner(entity)   user.uid == entity.owner_id     anything
member(wid)     user.wid == entity.wid          world
anyone          is_authenticated                -
"""
import uuid


def verify(policy, user, entity=None):
    if user is None:
        return False
    elif 'admin' == policy:
        # we already determined that user is not an admin
        return hasattr(user, 'admin') and user.admin
    elif 'me' == policy:
        if isinstance(entity, str):
            entity = uuid.UUID(entity)

        if isinstance(entity, uuid.UUID):
            return user.uid == entity
        else:
            return user.uid == entity.uid
    elif 'king' == policy:
        return entity.iso == user.iso and entity.wid == user.wid
    elif 'member' == policy or 'in world' == policy:
        return entity.wid == user.wid
    elif 'worldless' == policy:
        return user.wid is None
    elif 'owner' == policy:
        return entity is not None and entity.owner_id == user.uid and entity.wid == user.wid
    elif 'anyone' == policy:
        return user.is_authenticated
    else:
        raise Exception("Policy not found: {}".format(policy))


def can_edit(world: World, attr):
    if not hasattr(world, attr):
        return False

    if attr not in ['map', 'name', 'invlink', 'max_players']:
        return False

    return True

from .config import Config
from .get_tsxs import get_tsxs
from uuid import uuid4


def rollback(dir='.'):
    for file_name in get_tsxs(dir):
        print(file_name)
        with open(file_name) as file:
            file_body = file.read()

        idx = 0
        while (idx := file_body.find(f' {Config.ATTR}=', idx + 1)) != -1:
            mark_start = idx
            mark_end = mark_start + len(Config.ATTR) \
                       + len('="') + len(Config.ATTR_PREFIX) + len(str(uuid4())) + len('" ')

            mark_id_start = mark_start + 1 + len(Config.ATTR) + len('="')
            mark_id_prefix = \
                file_body[mark_id_start:mark_id_start + len(Config.ATTR_PREFIX)]

            if mark_id_prefix == Config.ATTR_PREFIX:
                file_body = file_body[:mark_start] + file_body[mark_end:]

        with open(file_name, 'w') as file:
            file.write(file_body)

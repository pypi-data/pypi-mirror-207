#!/usr/bin/env python3
from typing import Dict
import json
import os
from eia.utils.constants import ODIN_DB

CREDS_PATH: str = os.path.join(os.path.expanduser("~/"), "credentials.txt")
CREDENTIALS: Dict = {'MYSQL_USER': 'admin',
                     'MYSQL_PASSWD': 'A10ThunderBolt!!',
                     'MYSQL_HOST': ODIN_DB,
                     'MYSQL_DB': 'odin'}


def load_credentials() -> bool:

    if not os.path.exists(CREDS_PATH):
        with open(CREDS_PATH, 'wt') as f:
            f.write(json.dumps(CREDENTIALS))
        f.close()

    try:
        for k, v in json.loads(open(CREDS_PATH, 'rt').read()).items():
            os.environ[k] = v
        return True

    except:
        return False

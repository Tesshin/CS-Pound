import os


class Constants:
    prefix = ','
    discord_token = os.environ.get('discord', None)
    osu_api_key = os.environ.get('osu', None)
    support_server_link = 'https://invite.gg/cspound'
    version = '2.3'
    invite_link = 'https://www.tailstar.us/'
    mongodb_uri = os.environ.get('mongodb', None)
    database_name = 'cs_pound'
    osu_collection_name = 'osu_profiles'
    autoremind_collection_name = 'auto_remind'

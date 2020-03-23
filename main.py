import local_settings as settings
from task import login, coment_in_forum_per_week, create_forum_per_week

login(settings.USERNAME, settings.PASSWORD)
# message = 'Setiap mahasiswa cukup berdiskusi di satu forum saja (bebas).'
# create_forum_per_week(settings.COURSE_IDS, 3)
# coment_in_forum_per_week(settings.COURSE_IDS, 3, message)

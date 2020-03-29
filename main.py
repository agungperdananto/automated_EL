import local_settings as settings
from task import login, coment_in_forum_per_week, create_forum_per_week

login(settings.USERNAME, settings.PASSWORD)
for week in settings.COURSE_SECTION:
    create_forum_per_week(settings.COURSE_IDS, week)
    coment_in_forum_per_week(settings.COURSE_IDS, week, settings.COMMENT_MESSAGE)
print('Done')

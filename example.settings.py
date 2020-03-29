from sqlalchemy import create_engine
# DB Settings
DB_ENGINE = ''
DB_HOST = ''
DB_USER = ''
DB_PASSWORD = ''
DB_PORT = ''
DB_NAME = ''


engine = create_engine('{}://{}:{}@{}:{}/{}').format(
    DB_ENGINE,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

# Daftar Pertanyaan untuk forum
FORUM_QUESTIONS = [
]

LOGIN_URL = 'https://e-learning.unpam.ac.id/login/index.php'
USERNAME = ''
PASSWORD = ''

COURSE_URL = 'https://e-learning.unpam.ac.id/course/view.php?id={}#section-{}'

# Daftar Course ID
COURSE_IDS = []
COURSE_SECTION = []

FORUM_URL = 'https://e-learning.unpam.ac.id/mod/forum/view.php?id={}'

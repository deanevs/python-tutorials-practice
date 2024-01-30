## https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

settings.py is what you would typically use to setup a project.  The issue of course is that if you commit to Git then 
it will be visible to all shared

1. import python-decouple
2. create .env file and put constants and secrets in there
3. from decouple import config in program
4. reference by config('LABEL')

### Notes:

Use cast to ensure correct types

DEBUG = config('DEBUG', cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)


ALLOWED_HOSTS=.localhost, .herokuapp.com

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

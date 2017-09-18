# Facebook Msg

verify_token = 'YOUR_VERIFY_TOKEN'
token = "YOUR_TOKEN"

# Database

DATABASE_NAME = 'yumngein'
DATABASE_USER = 'yumngeinadmin'
DATABASE_HOST = 'localhost'
DATABASE_PASSWORD = 'myBestPassword'
DATABASE_STRING_FORM = "postgresql://{}:{}@{}:5432/{}"
DATABASE_STRING = DATABASE_STRING_FORM.format(DATABASE_USER, DATABASE_PASSWORD,
                                              DATABASE_HOST, DATABASE_NAME)


def getDatabaseString():
    return DATABASE_STRING

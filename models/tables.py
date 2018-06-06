# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

def get_user_email():
    return auth.user.email if auth.user is not None else None
def get_user_name():
    return auth.user.first_name if auth.user is not None else None 


db.define_table('checklist',
                Field('user_email', default=get_user_email()),
                Field('user_name', default=get_user_name()),
                # Field('title'),
                Field('phone', 'integer'),
                # Field('memo', 'text'),
                Field('gpa','double'),
                Field('income','double'),
                Field('family_members','integer'),
                Field('race','string'),
                Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
                Field('is_public', 'boolean', default=False)
                )

db.define_table('scholarships',
                Field('user_email', default=get_user_email()),
                Field('scholarship_name'),
                Field('information', 'text'),
                Field('scholarship_url'),
                Field('contact_name'),
                Field('contact_email'),
                Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
                Field('is_public', 'boolean', default=False)
                )
db.checklist.user_email.writable = False
db.checklist.user_email.readable = False
db.checklist.updated_on.writable = db.checklist.updated_on.readable = False
db.checklist.id.writable = db.checklist.id.readable = False
db.checklist.is_public.writable = False
db.checklist.is_public.readable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

UPDATE auth_user
SET first_name = 'ADMIN', last_name= 'USER'
WHERE is_superuser = 1;
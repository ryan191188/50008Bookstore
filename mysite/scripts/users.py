from  django.contrib.auth.models import User
def run():
    # Get all users
    # users = User.objects.all()
    # user = users[1]
    # user.set_password('dily1234')
    
    user1 = User.objects.create_user(
        username='xiexin2011@gmail.com',
        email='xiexin2011@gmail.com',
        is_superuser=0,
        first_name='',
        last_name='',
        is_staff=0,
        is_active=1,
        password='1TJT599QE2'
    )
    user2 = User.objects.create_user(
        username='huangran1991@yahoo.com',
        email='huangran1991@yahoo.com',
        is_superuser=0,
        first_name='',
        last_name='',
        is_staff=0,
        is_active=1,
        password='CV3MVFY68O'
    )

    
    user1.save()
    user2.save()
from django.contrib.auth import get_user_model 
User = get_user_model() 
User.objects.create_superuser('admin', 'admin@example.com', '12345678hr#')
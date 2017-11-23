from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            role=None,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
	name = models.CharField(('Name'),max_length=30, blank=True, null=True)
	phone_no = models.IntegerField(max_length=30,blank=True, null=True)
	email = models.EmailField(('email address'), max_length=155,unique=True, null=True, blank=True)
	is_active = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	created_on = models.DateTimeField(('Date joined'), default=timezone.now)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = MyUserManager()

	class Meta:
	    verbose_name = 'user'
	    verbose_name_plural = 'users'

	def get_full_name(self):
	    full_name = '%s %s' % (self.first_name, self.last_name)
	    return full_name.strip()

	def get_short_name(self):
	    return self.first_name

	def get_email(self):
	    if self.email is not None:
	        return self.email
	    return None



	@property
	def is_staff(self):
	    return self.is_superuser


class Article(models.Model):
    # The title of the Article
    title = models.CharField(max_length=255)
    # The author of the Article
    author = models.CharField(max_length=255)
    # The actual article content
    content = models.TextField()
    # Publication date
    pub_date = models.DateTimeField('publication date')
    # The category of the article
    category = models.CharField(max_length=255)
    # The amount of likes for the article
    likes = models.IntegerField()


'''class Comments (models.Model):
    #FK User
    user = models.ForeignKey('User')
    #FK Article
    article = models.ForeignKey('Article')
    #User comment
    commentContent = models.TextField()'''


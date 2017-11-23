from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    # ===========================================================================
    # overriding built in user manager
    # ===========================================================================

    # use_in_migrations = True

    def _create_user(self, email, password, is_superuser,  **extra_fields):
        # =======================================================================
        # creates user with given email and password
        # =======================================================================
        now = timezone.now()

        # if extra_fields['profile_pic'] == 'user_pic.png':
        #     extra_fields['profile_pic'] = ''
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True,
                          is_superuser=is_superuser,
                          created_on=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class MyUser(AbstractBaseUser,PermissionsMixin):
	first_name = models.CharField(('first name'),max_length=30, blank=True, null=True)
	last_name = models.CharField(('last name'), max_length=30,blank=True, null=True)
	email = models.EmailField(('email address'), max_length=155,unique=True, null=True, blank=True)
	is_active = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	created_on = models.DateTimeField(('Date joined'), default=timezone.now)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

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


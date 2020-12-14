 # Profiles REST API
------------------------------------------------------------------

 # VAGRANT

-  Vagrant is used to create a local development server . 
-  It allows to define the type of server for the application .
-  File is created through Vagrant CLI
-  Vagrant works by creating a bi-synchronized directory on vagrant server, that updates itself with all of the changes from host
   folder and vice versa.

   **Pre-requisite for Vagrant CLI to inititate**
   
-  (On Windows set Windows Power shell path before vagrant up)  
     PATH = C:\Windows\System32\WindowsPowerShell\v1.0 ;

   **Create Vagrant file**

*  Steps to create Vagrant file 
   cmd -> vagrant init <servername/servertype>
        eg : vagrant init ubuntu/bionic64

*  Below url can be used to search about box
         https://vagrantcloud.com/search        
   
    (Other required configuration of a Vagrantfile can be copied from this project)

*  **Run Vagrant file**

   Since the box is a completely different isolated box on the host machine , hence SSH is required to connect .
    
   To Connect  ->
     vagrant ssh  (required vagrant up to run first) 

   On successfully connected ->
     terminal usercmd changes to -> "vagrant@ubuntu-bionic:~$" , i.e. Server is up and running.

   To Disconnect ->
     exit  
   
   **See Vagrant UI**

     config.vm.provider :virtualbox do |vb|
     vb.gui = true

     Note: If vagrant server doesnt gets started, then
       -> open the virtual box (oracle) -> open settings for the project -> in advanced (select cable connect)

   **Vagrant synced folder**

   Switch to "vagrant" folder on the terminal.

    vagrant@ubuntu-bionic:~$ cd /vagrant
    vagrant@ubuntu-bionic:/vagrant
       

   **RUN CODE FROM HOST TO VAGRANT SERVER**

    vagrant@ubuntu-bionic:/vagrant$ python3 hello_world.py


----------------------------------------------------------------------------------------------------------------------------------------

# PYTHON ENV ON VAGRANT SERVER

-   At times if we want to re create the vagrant server and use the new environment , Its important to create python environment on vagrant's home
    directory , i.e/. outside the "vagrant" directory on vagrant server , so as to avoid synchronization for environment files.

     sudo apt-get install python3-venv - (Install python3-env if Required)

-   Creating the virtualEnvironment
      vagrant@ubuntu-bionic:/vagrant$ python -m venv ~/<env_name>    -- python/python3 -- <env_name> = django_env

-   Activate the virtual environment 
      vagrant@ubuntu-bionic:/vagrant$ source ~/djangoenv/bin/activate
      
      after successful activation ->  (djangoenv) vagrant@ubuntu-bionic:/vagrant$

-   Deactivate the virtualEnvironment

      deactivate

---------------------------------------------------------------------------------------------------------------------------------------------         
# PYTHON LIBRARIES ON PYTHON ENVIRONMENT THROUGH REQUIREMENTS.TXT file

      django
      djangorestframework

-----------------------------------------------------------------------------------------------------------------------------------------------

# LOADING THE FRAMEWORK DEPENDENCIES ON VIRTUAL ENVIRONMENT

   Prequiste folder & state -> 

      (djangoenv) vagrant@ubuntu-bionic:/vagrant$ pip install -r requirements.txt

-----------------------------------------------------------------------------------------------------------------------------------------------

# CREATE NEW DJANGO PROJECT ON THE ROOT OF EXISTING DIRECTORY

      (djangoenv) vagrant@ubuntu-bionic:/vagrant$ django-admin.py startproject profiles_project .

-----------------------------------------------------------------------------------------------------------------------------------------------

# CREATE NEW DJANGO APP ON THE ROOT OF EXISTING DIRECTORY 

- A Django project can have multiple apps

      (djangoenv) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api

---------------------------------------------------------------------------------------------------------------------------------------------

# MANIPULATIONS IN SETTINGS.PY

- All the outer dependecy apps has to be added inside INSTALLED_APPS in settings.py of django_project (here - profiles_project)

  eg:    
    INSTALLED_APPS = [
      'rest_framework',
      'rest_framework.authtoken',
      'profiles_api',
   ]

---------------------------------------------------------------------------------------------------------------------------------------------

# RUN THE DEVELOPMENT SERVER

   python manage.py runserver 0.0.0.0:8000

---------------------------------------------------------------------------------------------------------------------------------------------

# Create Models

   **Django has default user Model and Django Admin**

      To use the default user Model , django suggest below imports 
       
         from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

---------------------------------------------------------------------------------------------------------------------------------------------

# Create Models  

   eg: 
     class UserProfile (AbstractBaseUser, PermissionsMixin):
        """Database model for users in the system"""
        email = model.EmailField(max_length=255, unique=True)
        name = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(defaut=False)

---------------------------------------------------------------------------------------------------------------------------------------------

# Create Model Manager        
 
 - Model Manager helps Django to work with custom models with the command line tools
 - Basically it has the helper methods for the model.

---------------------------------------------------------------------------------------------------------------------------------------------

# Advice Django to use UserProfile entity as the USER MODEL 

 - In settings.py ,
     AUTH_USER_MODEL = 'profiles_api.UserProfile'

---------------------------------------------------------------------------------------------------------------------------------------------

# Django Migrations File

  * Pre-requisite to make migrations
    - vagrant server should be up and running -(vagrant up & vagrant ssh)
    - environment should be activted -(source ~/djangoenv/bin/activate)


 - The way Django manages the database is through migration file.
 - It containes all the migration required to be process to match the database with the updated django models 
 - So every time , a model is changed or newly models are added , a new migration file has to be genrated and pushed

   **To create Migration file specifically for a project**

      - python manage.py makemigrations <app_name>
        eg - python manage.py makemigrations profiles_api - (generates the migration file for updated models )
      - It generates a file alike -0001_initial.py      
   
   **To run Migration file for entire project**
     
      - python manage.py migrate


---------------------------------------------------------------------------------------------------------------------------------------------  

# Set Custom User Model
    
- Import used in the model class 
       - from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

- This advices the django to use UserProfile entity in profile_api to use for all authentication and user registration.
     - AUTH_USER_MODEL = 'profiles_api.UserProfile'

---------------------------------------------------------------------------------------------------------------------------------------------  

# Creating superuser by using Django command line tool.

  - Make sure vagrant server is up and running and the virtual environment is up and running.

  **Command to create super user**
   
    cmd : python manage.py createsuperuser
  
    - requires email 
    - requires name 
    - requires password





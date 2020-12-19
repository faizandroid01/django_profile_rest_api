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
  
    - requires email - (here : faizrocks9211@gmail.com)
    - requires name - (here : faiz)
    - requires password - (here : faiz123)


---------------------------------------------------------------------------------------------------------------------------------------------  

# Registering models in admin for an app

  **Command to create super user**

     cmd : admin.site.register(models.UserProfile)

     - import models from project app 

---------------------------------------------------------------------------------------------------------------------------------------------  

# APIVIEWS 

  - An ApiView allows us to define methods that matches standard Http methods.
  - Gives the most of the control over logic (can be considered as service class as in Java)
    - Perfect for implementing logic
    - Calling other API's
    - Working with local files

    **Example1**

        def get(self ,request ,format=None):
            """Return one or more items"""
            return Response({'list': 'items'})

        similarly:
            def post(self ,request ,format=None):
            def put(self ,request ,format=None):
            def patch(self ,request ,format=None):
            def delete(self ,request ,format=None):         

    **Example2**

        from rest_framework.views import APIView
        from rest_framework.response import Response
        

        class HelloApiView(APIView):
        """APi View to test Hello World"""

        def get(self, request ,format=None):
            """Test an APIView"""
            an_apiview = [
                'Uses HTTP functions as method (get, post, put ,patch, delete)',
                'Is similar to a traditional Django view',
                'gives the most control over your application logic',
            ]

            return Response({'message':'Hello!', 'an_apiview': an_apiview })
  
    **Example3 With Serializer validation**

        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status

        class HelloApiView(APIView):
        """APi View to test Hello World"""

        serializer_class = serializers.HelloSerializer

        def post(self,request):
           """Creates a hello message with our name"""

           serializer = self.serializer_class(data=request.data)

           if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response ({'message': message})
            else:
                return Response(serializer.errors,status = status .HTTP_400_BAD_REQUEST)

 
---------------------------------------------------------------------------------------------------------------------------------------------  

# URLS.PY for an PROJECT_APP 

  - file manages all the call for various functions of apiview of a certain project (can be a project or an app)
  - .as_view -> django renders the view from views 

  **Example**

      from django.urls import path
      from profiles_api import views

      urlpatterns = [
          path('hello-view/', views.HelloApiView.as_view()),
      ]

  **Example2**

      from django.urls import path, include
      from . import views
      from rest_framework import routers

      router = routers.DefaultRouter()
      router.register('courses',views.CourseView)

      urlpatterns = [
        path('',include(router.urls)),
      ]

  **TEST FOR APIVIEW**    

      - Run Server nd hit the api at 
          http://localhost:8000/api/hello-view/

---------------------------------------------------------------------------------------------------------------------------------------------

# SEARIALIZERS 

   - is a feature from the Django Framework , that converts the input in to python object and vice versa.
   - It is required to access the 'post' or 'put' request content from the data input.
   - it also validates the input of the request models , i.e it passess through some certain validation rules

   **Example1**

      from rest_framework import serializers

      class HelloSerializer(serializers.Serializer):
          """Serializes a name field for testing our APIView"""
          name = serializers.CharField(max_length=10)  => (This seriralizer field "name" is mandated to be a CharField of 10 length )
    
---------------------------------------------------------------------------------------------------------------------------------------------

# WORK FLOW

   **Without Serializer**
      MODEL* => ApiView => App {Urls.py} => Projects {Urls.py} .

   **With Serializer**
      MODEL* =>Serializer => ApiView => App {Urls.py} => Projects {Urls.py} .

    '*' can be or cannot be part, only api view and its registration in the urls.py @appLevel and @projectLevel is responsible for an API run
    

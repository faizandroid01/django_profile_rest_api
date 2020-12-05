 # Profiles REST API
------------------------------------------------------------------

 # VAGRANT

-  Vagrant is used to create a local development server . 
-  It allows to define the type of server for the application .
-  File is created through Vagrant CLI
-  Vagrant works by creating a bi-synchronized directory on vagrant server, that updates itself with all of the changes from host
   folder and vice versa.
   
   **Create Vagrant file**

*  Steps to create Vagrant file 
   cmd -> vagrant init <servername/servertype>
        eg : vagrant init ubuntu/bionic64
   
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
      vagrant@ubuntu-bionic:/vagrant$ python -m venv ~/<env_name>    -- python/python3 -- <env_name> = djangoenv

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


    





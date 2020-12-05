# Profiles REST API

<!-------------------------------- VAGRANT ----------------------------------->

- Vagrant is used to create a local development server . 
- It allows to define the type of server for the application .
- File is created through Vagrant CLI
- Vagrant works by creating a bi-synchronized directory on vagrant server, that updates itself with all of the changes from host
  folder and vice versa.
   
   <!-- Create Vagrant file -->

* Steps to create Vagrant file 
   cmd -> vagrant init <servername/servertype>
        eg : vagrant init ubuntu/bionic64
   
    (Other required configuration of a Vagrantfile can be copied from this project)

   <!-- Run Vagrant file --> 

    Since the box is a completely different isolated box on the host machine , hence SSH is required to connect .
    
    To Connect  ->
     vagrant ssh  (required vagrant up to run first) 

     On successfully connected --> terminal usercmd changes to -> "vagrant@ubuntu-bionic:~$" , i.e. Server is up and running.

    To Disconnect ->
     exit  
   
   <!-- See Vagrant UI  --> 

     config.vm.provider :virtualbox do |vb|
     vb.gui = true

     Note: If vagrant server doesnt gets started, then
       -> open the virtual box (oracle) -> open settings for the project -> in advanced (select cable connect)

   <!-- Vagrant synced folder  --> 

    switch to "vagrant" folder on the terminal.

    vagrant@ubuntu-bionic:~$ cd /vagrant
    vagrant@ubuntu-bionic:/vagrant
       

<!-------------------------------- RUN CODE FROM HOST TO VAGRANT SERVER ----------------------------------->

# Docker_project_with_flask
### Docker_project_with_flask
<ol> 
We create a project, in which front page in the <strong>HTML language</strong> and the data will store in the <strong>docker database</strong>. We establish a connection between the <strong>HTML page</strong> and <strong>docker database</strong> with the help of <strong>python language (flask)</strong>.  In this case, the <strong>flask</strong> is used to make the connection between the <strong>docker database and HTML page</strong>.</br>

<li><strong>First step</strong> :- Create front page in <strong>HTML language(register.html)</strong>.</li>

<li><strong>Second step</strong> :- Create connection page in <strong>python language</strong>.<li>
<li>We will create a connection page with the help of <strong>flask</strong> and in this page we need:-</li>
<ol>
<li><strong>SOLAlchemy </strong>:- use to make a connection between python and database.<li>
<li><strong>app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@db:3306/my_db'</strong></li>
<strong>app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:'password'@db:port for database/name_of_database'</strong></br> 
<strong>NOTE:- </strong>/Before running this project we need to create a database in the <strong>docker database(mysql)</strong></br>
<li><strong>class User(db.Model)</strong> :-Now we need to define the name of the table and also provide the columns name with the required attributes.</li>
<li>Use <strong>post method()</strong> to get data from front page.</li>
</ol>

<li><strong>Third step </strong>:- open terminal and create new folder in which you have to save templates and python file</br>
<strong>$ mkdir docker_register</strong></br>
mkdir folder_name</li>

<li>Now in this folder create a <strong>virtual environment</strong> because, it helps us to create and manage a separate environment for your python project.</br>
<strong>$ pip install virtualenv</strong></br>
<strong>$ python3 -m venv env (env = name of environment)</strong></br>
<strong>$ source env/bin/activate</strong></br></li>

<li>Now we need to create a <strong>dockerfile</strong> :- </br>
  in this file we have to define.</li>
  <ol>
<li><strong>'from'</strong> will define in which base we are creating an image like:-</br>
<strong>FROM ubuntu:16.04</strong></li>
<li><strong>RUN command</strong> is used to run instructions against the image. In our case, we first update our Ubuntu system and then install the <strong>python-pip python</strong> and <strong>libmysqlclient</strong> on our ubuntu image.</li>
<li><strong>COPY :- provide project name with './'</strong></li>
<li><strong>WORKDIR :- which project is working </strong></li>
<li>Run requirement file :-<strong> RUN pip install -r requirements.txt</strong></li>
</ol>
```
FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y libmysqlclient-dev

COPY . /docker_register
WORKDIR /docker_register

RUN pip install -r requirements.txt



```


<li>We need to create a new txt file <strong>'requirements.txt'</strong></br>
In this file, we will store all the requirements that we required to run this project.</br>
use commands to freeze requirements</br>
<strong>$ pip freeze > requirements.txt</strong></li>
```
Click==7.0
Flask==1.0.2
Flask-SQLAlchemy==2.3.2
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.1
mysql==0.0.2
mysqlclient==1.4.2.post1
SQLAlchemy==1.3.2
Werkzeug==0.15.1

```

<li>Now to run our project and save content in database, we need a <strong>docker-compose.yml</strong> file in which :-</br>
we will provide details about <strong>database</strong> and web <strong>(project details)</strong></li>
<ol>
<li>image=mysql use for database</strong></li>
<li>restart it always</li>
<li>Provide a password for mysql.</li>
</ol>
```

    db:
      image: mysql
      restart: always
      environment:
        MYSQL_ROOT_PASSWORD: 123
      networks:
        - main
```

<li>In web:-</li>
<ol>
<li>project name = image: docker_register</li>
<li>name of python file (connection file)  command:  python app.py</li>
<li>docker port = ports- "2226:5000"</li>
</ol>
```
 web:
      restart: always
      image: docker_register
      command:  python app.py
      ports:
        - "2226:5000"
```

 
<li>Now we can run our project :-</br>
build an image of this project</br>
<strong>$ docker build -t docker_register:latest . <strong></li> 
  
 ![built](https://user-images.githubusercontent.com/47202519/56130684-34b38900-5fa3-11e9-9abc-a3a554ec3ecb.png)


<li>Run compose file to run the project</br>
<strong>$ docker-compose up</strong></li>    

![comp](https://user-images.githubusercontent.com/47202519/56130881-b4d9ee80-5fa3-11e9-96bb-8f3cef71e8e0.png)


<li>Now check the error :- database is not defined</br>
<strong>sqlalchemy.exc.OperationalError: (MySQLdb._exceptions.OperationalError) (1049, "Unknown database 'my_db'")</strong></li>

<li>Open another terminal <strong>(ctrl+shift+t)</strong> and create database.</li>
<ol>
<li>Check all containers</br>
<strong>$ docker ps -a</strong></li>  

![ps](https://user-images.githubusercontent.com/47202519/56131147-4d706e80-5fa4-11e9-96aa-7107151d1862.png)
<li>Need to create database with the help of mysql container name.</br>
 <strong>$ docker exec -it dockerregister_db_1 bash</strong></br>
 Use <strong>mysql-query</strong> to create database</li>  

![data](https://user-images.githubusercontent.com/47202519/56131388-e3a49480-5fa4-11e9-9693-f00e88c80f10.png)

</ol>

<li>now run docker-compose up command</li>
<ol>
<li><strong>$ docker-compose up</strong></li>
Open another terminal</br>
<li><strong>$ docker ps -a</strong></li>
check project status and run port in a browser <strong>'0.0.0.0:2226'</strong></br>
fill the form and check database.</li>
</ol>

### Upload image on docker hub
<ol>
<li>Docker Hub is the place where open Docker images are stored.</br>
we need to create an account on <strong>https://hub.docker.com/.</strong> After verifying your email you are ready to go and upload your first docker image.</li>
<ol>
<li>Log in on <strong>https://hub.docker.com/</strong></li>
<li>Click on <strong>Create Repository.</strong></li>
<li>Log into the Docker Hub from the command.</li>
</ol>
<li><strong>$ docker login</strong> or</br>
  <strong>$ docker login --username=docker_hub_username</strong> or</br>
  <strong>$ docker login --email=_@_.com</strong></li>  
  
 ![login](https://user-images.githubusercontent.com/47202519/56132417-89590300-5fa7-11e9-87bf-0696719a9e34.png)

<li>Check the image ID that we want to push </br>
<strong>$ docker image</strong></br>  

![img](https://user-images.githubusercontent.com/47202519/56132876-c245a780-5fa8-11e9-9145-aba5de9aa499.png)

Now we need repository_name and image_id that we have want to push.</br>
docker tag image_id docker_hub_username/repository_name:any_tag</br>
<li><strong>$ docker tag e957c6fa720  sayakasta/docker_register:firsttry</strong></li>  

![uplo](https://user-images.githubusercontent.com/47202519/56133202-7d6e4080-5fa9-11e9-95fd-17aa85088ca0.png)

<li>Push your image to the repository you created</br>
<strong>docker push docker_hub_username/repository_name</strong></br>
now image is available for everyone to use.</li>
</ol>

### Save image from docker hub and run it.
<ol>
<li>To run this project we need to share <strong>docker-compose.yml</strong> file but, we need to make some changes in this file.</br>
<li>Make changes in web :- image:provide_name_of_docker_hub_images</li>
<li>images: docker_hub_username/repository_name:any_tag</li>
<li>To run the project in any other system we need to share and run the docker-compose.yml file with docker command</li>
```
 web:
      restart: always
      image: sayakasta/docker_register:firsttry
      command:  python app.py
      ports:
        - "2226:5000"
      links:
        - db

```
</ol>
<ol>



 

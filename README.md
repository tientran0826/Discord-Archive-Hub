# DISCORD ARCHIVE HUB

## Introduction
The Discord Archive Hub is utilized to create channel threads on a dedicated website for the purpose of storing data, including images, videos, documents, and more, which are received through a Discord Bot. To limit storage capacity, the data is stored using direct links from Discord, but they are categorized into images, documents, and URLs based on their content. The website is built using the Flask framework and SQLAlchemy, along with the Discord API for constructing a Chat Bot as the primary means of data transmission.

## Live Demo
Live demo deploy with AWS ECS and AWS RDS </br> <br>
[Web Demo](http://ec2-3-237-253-23.compute-1.amazonaws.com/)
[Invite Bot](https://discord.com/oauth2/authorize?client_id=1111854391209766932&permissions=8&scope=bot)

## Database Config
Change this line in **app/__init__.py**
<pre>DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'database.db') </pre>
to
<pre>DATABASE_URL = "mysql://root:password@hostname/databasename" </pre>


## Discord Token Config
Config the token in **.env** file.
<pre># .env
DISCORD_TOKEN=YOUR_TOKEN_HERE</pre>
## Bot Commands 
  Default prefix: **=**
  + createChannel + (Channel_name) : Create a thread on website <br><br>
  ![img1](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/create_channel_1.png?raw=true) <br><br>
  ![img2](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/create_channel2.png?raw=true) <br><br>
  + post + (id_channel) + (content): Send content to the channel <br><br>
  ![img3](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/post_1.png?raw=true) <br><br>
  ![img4](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/post_2.png?raw=true) <br><br>
  ![img5](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/post_3.png?raw=true) <br><br>
  + setprefix + (new_prefix): Change prefix to new prefix

## Admin Panel
Your admin panel (using to control the records) <br><br>
![img6](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/panel.png?raw=true) <br><br>

<pre>yourdomain/panel </pre>
Default admin account
<pre>username: admin, password: admin </pre>
![img7](https://github.com/tientran0826/Discord-Archive-Hub/blob/main/images/panel_1.png?raw=true) <br><br>


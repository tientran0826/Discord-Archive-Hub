
import discord,os
from flask import Flask,redirect,url_for,request
from discord.ext import commands
from flask_admin import Admin,AdminIndexView
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_login import LoginManager,current_user,login_user,logout_user

app = Flask(__name__)
intents = discord.Intents().all()
client = discord.Client(intents=intents)
login = LoginManager(app)

basedir = os.path.abspath(os.path.dirname(__file__))
#DATABASE_URL = "mysql://root:password@hostname/databasename"
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.update(
    TESTING=True,
    SECRET_KEY='70cd3de994553cecc6d0e30a27f4c064'
)

db = SQLAlchemy(app)
from app.models import *


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next_page=request.endpoint))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next_page=request.endpoint))

admin = Admin(app = app,name='Mương 14',index_view=MyAdminIndexView(url="/panel"))
admin.add_view(MyModelView(User,db.session))
admin.add_view(MyModelView(Channel,db.session))
admin.add_view(MyModelView(Post,db.session))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))

#Set Prefix
prefix = ["="]
custom_prefixes = {}
async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, prefix)
    else:
        return prefix

client = commands.Bot(command_prefix = determine_prefix,
                      case_insensitive=True,
                      intents=intents,
                      )
@client.command()
@commands.guild_only()
async def prefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or prefix
    await ctx.send(f"Set prefix into `{prefixes}` ")



from . import routes






from app import app,client,db,discord
from app.models import Channel,Post,User
from threading import Thread
import re
import dotenv,os

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

def run():
    with app.app_context():
        # Restart database when restarting server
        db.drop_all()
        db.create_all()

        # Create default account for admin
        admin_account = User(username="admin", password="admin", email="admin")
        db.session.add(admin_account)
        db.session.commit()

    app.run(host='0.0.0.0',port=8000)

@client.command()
async def createChannel(ctx,*,channel_name):
    with app.app_context():
        try:
            new_channel = Channel(channel_name = channel_name)
            db.session.add(new_channel)
            db.session.commit()
            await ctx.send("Tạo channel thành công!")
        except:
            await ctx.send("Có lỗi trong việc tạo channel, có thể channel đã tồn tại !")

def find_URL(txt):
  if txt == None: return None
  url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',txt) 
  return str(url)


@client.command()
async def post(ctx,channel_id,*,arg = None):
    with app.app_context():
        channel_ids = [channel.id for channel in Channel.query.all()]
        try:
            attachment_link = []
            for attachment in ctx.message.attachments:
                attachment_link.append(attachment.url)
            if int(channel_id) in channel_ids:
                new_post = Post(channel_id = int(channel_id), username = str(ctx.message.author),description = arg , attachments = str(attachment_link), links = find_URL(arg))
                db.session.add(new_post)
                db.session.commit()

                await ctx.send("Thêm post thành công vào ``{}`` .".format(Channel.query.get(int(channel_id)).channel_name))
            else:
                await ctx.send("ID channel không hợp lệ.")
        except:
            await ctx.send("ID channel không hợp lệ.")

@client.command()
async def channel(ctx):
    text = """"""
    embed = discord.Embed(title='Channels')
    with app.app_context():
        channels = Channel.query.all()
        
        for channel in channels: 
            text += str(channel.id) + ". " + channel.channel_name + "\n"

    embed.add_field(name = 'ID và tên channel', value = text)
    await ctx.send(embed = embed)


if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    client.run(TOKEN)

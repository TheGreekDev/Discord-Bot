import discord as Discord;

Clients = Discord.Client();

@Clients.event
async def on_ready():
    Activity = Discord.Game(name = 'Nothing...', type = 3);
    await Clients.change_presence(status =
    Discord.Status.online, activity = Activity);
    print('Logged in as: {0.user}'.format(Clients));

@Clients.event
async def on_message(message):
    if message.author == Clients.user:
        return;

    if message.content.startswith('!Hello'):
        await message.channel.send('Hello');

Clients.run('Token');

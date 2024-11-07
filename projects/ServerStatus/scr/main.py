from flask import Flask, request, jsonifys
import nextcord
from nextcord.ext import comman.
from config import servers


app = Flask(__name__)

bot = commands.Bot(command_prefix='/')


@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    data.get('tick')
    data.get('players')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    return 200

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name='start-server')  
async def greet(ctx, server: str):

    if not any((server.lower() == s for s in servers ))
        await ctx.send(f'{stormworks} is not a valid server mabye check your spelling? (case-insensitive)')

    await ctx.send('Hello! How can I assist you today?')

if __name__ == '__main__':
    app.run(debug=True)
    bot.run('YOUR_BOT_TOKEN')
    bot.add_command(submit_data)


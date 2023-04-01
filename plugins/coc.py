#@Ryu_god

from pyrogram import*
from timi import bot

@bot.on_message(filters.command('player'))
def get_player_info(_, message):
    player_name = message.text.split()[1]
    response = requests.get(f'https://api.clashofclans.com/v1/players/{player_name}', headers={'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM1NDMwMzdmLTBjODMtNDBkNC1iNGVhLTE4YjA0ZTU2ZGUwNyIsImlhdCI6MTY4MDMzMjE4OCwic3ViIjoiZGV2ZWxvcGVyLzJmYmVmZGJmLTg2MWUtY2RlOS0wY2M2LTE1ZGMwNjZhMDYxNSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEzNy45Ny43OC41MSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.t64BgE-XsZM3nBHm7qXogQ8Q4hcHPemALYlyM8CLbaw6cC671iEHnZd40KRyCDXe7jLEAC6BKSaodUh5NKclDg'})
    data = response.json()
    message.reply_text(f"information about {player_name}: {info}")

@bot.on_message(filters.command('clan'))
def get_clan_info(client, message):
    clan_tag = message.text.split()[1]
    data = response.json()
    message.reply_text(f"information about the clan: {info}")



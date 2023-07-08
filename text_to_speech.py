import requests
import json
import asyncio
from discord import FFmpegPCMAudio

async def text_to_speech(response, message):
    # Define the API endpoint
    url = "https://api.elevenlabs.io/v1/text-to-speech/yoZ06aMxZJJ28mfd3POQ"

    # Define the headers for the API request
    headers = {
        'xi-api-key': 'bcd357457ad91af98a43609c1f3467d6',
        'Content-Type': 'application/json'
    }

    # Define the body of the API request
    body = {
        "text": response,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    print("Sending voice message to ElevenLabs API.")
    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(body))

    # Save the response audio to a file
    with open('response.mp3', 'wb') as f:
        f.write(response.content)

    print("Saved voice response to file.")
    channel = message.author.voice.channel
    voice_channel = await channel.connect()

    # Delay for 2 seconds
    await asyncio.sleep(2)

    print("Playing voice response.")
    voice_channel.play(FFmpegPCMAudio(source="response.mp3"))

    while voice_channel.is_playing():
        await asyncio.sleep(1)
    await voice_channel.disconnect()

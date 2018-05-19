import os
import random

cwd = os.getcwd()
seasons = os.listdir(cwd)
episodes = []
seasonPath = ""
while True:
	season = random.choice(seasons)
	seasonPath = cwd+"/"+season
	if os.path.isdir(seasonPath):
		episodes = os.listdir(seasonPath)
		break

episodePath = ""
while True:
	episode = random.choice(episodes)
	extIndex = episode.rfind(".")
	extension = episode[extIndex:]
	episodePath = seasonPath+"/"+episode
	if extension in [".mkv", ".mp4", ".hvec"]:
		print episode
		break

episodePath = episodePath.replace(" ", "\\ ")
command = "vlc "+episodePath
print command
os.system(command)
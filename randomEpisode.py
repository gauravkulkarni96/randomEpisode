import os
import random

RECENT_LENGTH = 10
cwd = os.getcwd()
seasons = os.listdir(cwd)
episodes = []
seasonPath = ""
episodePath = ""
print "er"
while True:
	while True:
		season = random.choice(seasons)
		seasonPath = cwd+"/"+season
		if os.path.isdir(seasonPath):
			episodes = os.listdir(seasonPath)
			break

	while True:
		episode = random.choice(episodes)
		extIndex = episode.rfind(".")
		extension = episode[extIndex:]
		episodePath = seasonPath+"/"+episode
		if extension in [".mkv", ".mp4", ".hvec"]:
			print episode
			break
	recents = open(".recents", "r")
	recent_episodes = recents.readlines()
	print len(recent_episodes)
	if episodePath not in recent_episodes:
		if len(recent_episodes) >= RECENT_LENGTH:
			recent_episodes = recent_episodes[1:]
		recent_episodes.append(episodePath+"\n")
		recents = open(".recents", "w")
		recents.writelines(recent_episodes)
		recents.close()
		break

episodePath = episodePath.replace("~", "\~")
episodePath = episodePath.replace("$", "\$")
episodePath = episodePath.replace(" ", "\\ ")
command = "vlc "+episodePath
print command
os.system(command)
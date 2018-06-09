import os
import random

RECENT_LENGTH = 10
path = "/home/gaurav/Documents/Friends [chromium]"
seasons = os.listdir(path)
episodes = []
seasonPath = ""
episodePath = ""
print "er"
while True:
	while True:
		season = random.choice(seasons)
		seasonPath = path+"/"+season
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
	try:
		# series = path.split("/")[-1]
		recents = open(os.path.expanduser("~")+"/.recents", "r")
		recent_episodes = recents.readlines()
	except:
		recent_episodes = []
	# print len(recent_episodes)
	if episodePath not in recent_episodes:
		if len(recent_episodes) >= RECENT_LENGTH:
			recent_episodes = recent_episodes[1:]
		recent_episodes.append(episodePath+"\n")
		recents = open(os.path.expanduser("~")+"/.recents", "w")
		recents.writelines(recent_episodes)
		recents.close()
		break

episodePath = episodePath.replace("~", "\~")
episodePath = episodePath.replace("$", "\$")
episodePath = episodePath.replace(" ", "\\ ")
command = "vlc "+episodePath
os.system(command)
#!/usr/bin/env python2
import os
import random
import sys

RECENT_LENGTH = 10
VIDEO_FORMATS = [".mkv", ".mp4", ".hvec", ".mov", ".wma", ".wmv"]

TV_SERIES_PATHS = {
	"friends" : "/home/gaurav/Documents/Friends [chromium]"
	}

def selectEpisode(path):
	seasons = os.listdir(path)
	episodes = []
	seasonPath = ""
	episodePath = ""
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
			if extension in VIDEO_FORMATS:
				break
		try:
			series = path.split("/")[-1]
			recents = open(os.path.expanduser("~")+"/.recents"+series, "r")
			recent_episodes = recents.readlines()
		except:
			recent_episodes = []
		if episodePath not in recent_episodes:
			if len(recent_episodes) >= RECENT_LENGTH:
				recent_episodes = recent_episodes[1:]
			recent_episodes.append(episodePath+"\n")
			recents = open(os.path.expanduser("~")+"/.recents"+series, "w")
			recents.writelines(recent_episodes)
			recents.close()
			break

	episodePath = episodePath.replace("~", "\~")
	episodePath = episodePath.replace("$", "\$")
	episodePath = episodePath.replace(" ", "\\ ")
	command = "vlc "+episodePath
	os.system(command)
	return

if __name__ == "__main__":
	series = ""
	if len(sys.argv) == 1:
		selectEpisode(TV_SERIES_PATHS["friends"])
	else:
		series = sys.argv[1]
		if series.lower() in TV_SERIES_PATHS:
			selectEpisode(TV_SERIES_PATHS[series.lower()])
		else:
			print "{} name does not exist in TV_SERIES_PATHS".format(series)
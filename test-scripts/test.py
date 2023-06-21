import sheetmusicclassifier as smc
import utils
import os

inputFiles = [
    "/Users/jacob/Documents/Git Repos/MusicScoreClassifier-jh/test-scripts/input/a-score.jpeg",
    "/Users/jacob/Documents/Git Repos/MusicScoreClassifier-jh/test-scripts/input/not-a-score.jpeg"
]

model = "/Users/jacob/Documents/Git Repos/MusicScoreClassifier-jh/test-scripts/model/mobilenetv2.h5"

processed = smc.process(model, inputFiles)

for item in processed["images"]:
    print(item)

utils.writeJson(processed, os.path.join("/Users/jacob/Documents/Git Repos/MusicScoreClassifier-jh/test-scripts", "output.json"))
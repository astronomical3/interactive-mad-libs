#File for testing basic functionalities of story directory files and game file.
#If this test works, we can then use story_directory and game_file.py for actual stories.

from test_story_directory.test_story_list import *
from test_story_directory.test_stories import *
from test_story_directory.test_userq import *
from random import choice

choose_story_name = choice(STORYNAMES)
user_qs = STORYQUESTIONS[choose_story_name]

answerlist = []
for question in user_qs:
    answerlist.append(input(question))

choose_story = storiesdict(choose_story_name, answerlist)

print(choose_story)
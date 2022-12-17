from story_directory.story_list import *
from story_directory.stories import *
from story_directory.userq import *
from random import choice

choose_story_name = choice(STORYNAMES)
user_qs = STORYQUESTIONS[choose_story_name]

answerlist = []
for question in user_qs:
    answerlist.append(input(question))

choose_story = storiesdict(choose_story_name, answerlist)

print(choose_story)
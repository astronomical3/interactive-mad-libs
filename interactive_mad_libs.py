from story_directory.story_list import *
from story_directory.stories import *
from story_directory.userq import *
from random import choice

choose_story_name = choice(STORYNAMES)
user_qs = STORYQUESTIONS[choose_story_name]

answerlist = [input(question) for question in user_qs]
#for question in user_qs:
#    answerlist.append(input(question))

choose_story = story_choice(choose_story_name, answerlist)

#Used for testing if there are any stories that cause bugs:
print("Story name: {}".format(choose_story_name))

#Actual desired output:
print(choose_story)

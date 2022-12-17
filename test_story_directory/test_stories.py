def storiesdict(storyname, answerlist):
    storydictionary = {
        "test1" : "This is {}.".format(answerlist[0]),
        "test2" : "Hello, and welcome to {}.".format(answerlist[0]),
    }
    return storydictionary[storyname]

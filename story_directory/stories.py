def story_choice(storyname, answerlist):
    if storyname == "Vacations":
        return "A vacation is when you take a trip to some {} place with your {} family.  Usually, you go to some place that is near a/an {}, or up on a/an {}. A good vacation place is one where you can ride {} or play {} or go hunting for {}. I like to spend my time {} or {}. When parents go on a vacation, they spend their time eating three {} a day, and fathers play golf, and mothers sit around {}.  Last summer, my little brother fell in a/an {} and got poison {} all over his {}.  My family is going to go to (the) {}, and I will practice {}. Parents need vacations more than kids because parents are always very {} and because they have to work {} hours every day all year making enough {} to pay for the vacation.".format(*answerlist)
    elif storyname == "Principal for a Day":
        return "If I was principal of my school, I'd put {} and {} in every {} and have the cafeteria serve {} and {} for lunch. We would have '{} and Tell' every day, where students can bring {} and {} to share in class. Students would give teachers homework, like {}-page book reports about {} and {} math problems. Recess would last for {} hours, and instead of buses, I'd have {} and {} take the kids to and from school.".format(*answerlist)
    elif storyname == "Santa Claus Coming":
        return "Santa Claus is a {} man who wears a {} {} suit with a {} belt and a {} {} hat.  He has a long {} {} beard and his {} shakes like jelly when he laughs.  Every Christmas, he rides a {} full of presents, pulled by {} {} high into the night sky.  Santa {} down the chimney of people's homes to leave {}, {}, and {} under their Christmas trees.".format(*answerlist)
    elif storyname == "Valentines":
        return  "Valentine's Day is a great time to show all of your family and friends how much you {} them.  You can make {} for your mom, give a {} to your dad, and give your brother or sister a big pile of {}.  It can be fun to wear {} on Valentine's Day because it's the color of {}.  Don't forget your {} friends on {} either.  Even {} and {} like hugs and {}.  Especially on the biggest day of {} of the entire year!".format(*answerlist)
    elif storyname == "Lunchroom":
        return "Lunchtime in our cafeteria is always {}. They serve hot {} and {}, but some students {} their own {} to eat.  Some kids quietly {} their {}, while others throw {} or {} when the teachers aren't looking.  One time, a bunch of kids mixed all of their unfinished {} and {} together to make a {} mountain of {} on a {}. The teachers were {}, but everyone had already {} outside for recess, so nobody got in trouble.".format(*answerlist)
    elif storyname == "Halloween Monsters":
        return "Tonight is the night when all of the {} monsters come out to {}. {} witches with a big {} and {} shoes make potions and very spooky brews. Vampires with {} and long red capes visit with friends and search for neck capes. Ogres and ghosts sometimes {} and play, on this {} October day. All the trick-or-treaters {} and hunt for {} and a scare, dressed up as princesses and cowboys here and there.  Have a {} Halloween!".format(*answerlist)
    elif storyname == "Special Mother":
        return "My mother is {} because she {} care of me and always makes me {} {}. When I'm feeling {}, my mom {} me, and when I feel {}, she {} everything feel {}.  On my birthday, my mother {} my favorite meal, {} {} on a {}.  My mom always makes sure I {} my homework, {} my teeth, and {} my room. She has a way of always {} me feel {}, and that's why my mother is so {}.".format(*answerlist)
    elif storyname == "Twas Night Before":
        return "'Twas the night before {}, when all through the {}\nNot a creature was stirring, not even a {};\nThe {} were hung by the chimney with care\nIn hopes that {} would soon be there;\n\nThe children were nestled all snug in their {},\nWhile visions of {} {} in their heads;\nAnd mama in her kerchief, and I in my cap,\nHad just {} our brains for a {} winter's nap,\n\nWhen out on the {} there arose such a clatter,\nI {} from the {} to see what was the matter.\nAway to the {} I {} like a flash,\n{} open the {} and threw up the sash.\n\nThe {} on the breast of the {} snow\nGave the luster of midday objects below,\nWhen, what to my {} eyes should appear,\nBut a miniature {}, and eight {} {}.".format(*answerlist)
    elif storyname == "Birthday":
        return "Last week was my birthday. We went to my Grandma's house and had {} for supper. After that, we all sat in the {} to open my presents. The first gift was from my sister, and it was a {}. The next gift was from my mom and it was a(n) {} {}. The gift after that was a {}. I pretended to be happy--but I already had one of those! All of a sudden, I heard a strange noise. The noise was {} and I couldn't tell where it was coming from. I looked around the room. I stood up and walked {} to the {}. I looked in the {}. I looked under the {}. I found NOTHING! I realized that everyone in the other room was laughing! I asked my friend {}, 'What's going on?' I asked my other friend, {}. They just laughed. I asked {}, but they just {} around the room. I heard the noise again. Suddenly, it occurred to me -- the noise was coming from one of the presents! I opened the gift and inside the box was a baby {}! What a surprise!".format(*answerlist)
    elif storyname == "All About Me":
        return "Hi! My name is {}, and I have a secret to share with you. I'm a normal child by day, and a {} by night. Only you and my best friend {} knows my secret. You may be wondering how this happened. Well, one night, I was {} at home, and then BOOM! The lights went out and {} showed up. (S)he said in a booming voice, because your favorite color is {}, you have been chosen to be a {}. My mission is to save the people of {} by doing my favorite things: {}, {}, and {}. This may sound easy, but it is no walk in the park. It requires hard work and {}. My weakness is eating {}. They are GROSS! Keep that AWAY FROM ME! I save the world every night. But when I wake up in the morning, I go back to my normal life at school.".format(answerlist[0], answerlist[1], answerlist[2], answerlist[3], answerlist[2], answerlist[4], answerlist[1], answerlist[5], answerlist[6], answerlist[7], answerlist[8], answerlist[9], answerlist[10])
    elif storyname == "Bakery":
        return "CLERK: Good day, Miss. What can I do for you?\nCUSTOMER: I want to buy some {} bread.\nCLERK: Do you want a loaf of whole grain {}, or would you like some buttermilk {}?\nCUSTOMER: Just a regular loaf with sesame {} on it.\nCLERK: All right now, how about some nice {} cake?\nCUSTOMER: Well, I have {} children, and they all like to eat sweet {}. How much are your cookies?\nCLERK: We have {} chip cookies at {} dollars a pound. And we have this box of assorted little {} for only 2 dollars.\nCUSTOMER: I'll take one. They look like they don't have more than {} calories.\nCLERK: All right. That will be one box of {}, our special {} berry pie, and a big family-sized loaf of {}.".format(answerlist[0], answerlist[1], answerlist[2], answerlist[3], answerlist[4], answerlist[5], answerlist[6], answerlist[7], answerlist[8], answerlist[9], answerlist[10], answerlist[9], answerlist[11], answerlist[1])
    elif storyname == "Mountain Hike":
        return "Our {} are packed for a hike in the {} Mountains! We are carrying a picnic lunch with {} and {} on our {}, and I have a {} for {} photos. We will {} past meadows filled with {} and {} flowers, and pass a {} waterfall that sounds like a {}. Many animals live in the mountains, like the {} {} and {} {}. It's fun to {} them but important to be safe and keep a {} distance. The higher we {}, the smaller the wildflower meadow and waterfall appear; we may even see {} sill on the ground from last winter.".format(*answerlist)
    elif storyname == "Summer Camp":
        return "My family and I are going camping near a {} {} this summer.  Camping is {} because you get to {} and {} outside.  When we {} to the campground, we set up our {}, where we will {} at night.  We like to go {} in the {}, hoping to {} some {} for dinner.  We also go {} in the {} {}, hoping to spot wildlife like {} or {}.  My favorite part about camping is {} {} over the campfire.".format(*answerlist)
    elif storyname == "Silly Summer Goals":
        return "I could hardly believe it!  School was over and there were {} days of summer vacation to look forward to!  I couldn't wait to {} with my friends, {} in, and take a road trip to {}.  Of course, my {} didn't want me to waste the summer {} TV, so they helped me come up with a few summer goals:\n\t1.Read {} {}. \n\t2. Practice my {} for {} minutes each morning. \n\t3. Drink plenty of {} and learn to eat {} food. \n\t4. Start my own {} garden. \n\t 5. Practice {} the {} and learn to {} a(n) {} song. \n\t6. Go {}-watching with {}. \n\t7. Learn to slam-dunk a {} on a {}-foot hoop. \nThis is going to be one {} summer!".format(*answerlist)
    elif storyname == "Baltimore Trip":
        return "My family drove our {} to Baltimore last weekend to check out some of the sights and try some of those {} crabs we've heard so much about.  We started by going to the Inner {} and looking at the World Trade Center.  What a {} building!  Then, we {} to the National Aquarium and saw lots of {}.  The underwater {} show was {}!\nAfter all that sightseeing, we were hungry.  So, we took a {} to a restaurant in Little {} and ate lots and lots of {}.  We were stuffed after that, and decided to head back to the hotel.  It was a {} day out, so we walked back.  But {}!  Four {} tried to mug us!  My father tried to fight back, but he got hit in the {} with a {} and they took all our money.  Now we're {}!  I'm so tired from my trip to Baltimore, it was fun, but it's time to go home now!".format(*answerlist)
    

#More stories will be added in this function over time!
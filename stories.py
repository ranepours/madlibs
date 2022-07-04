class Story:
    def __init__(self, code, title, words, text):
        """create story words & template"""
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """push answers to text"""
        text = self.template
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        return text


# Here's a story to get you started
story1 = Story(
    "what if?",
    "If You Give A...",
    ["animal", "food_1", "noun_1", "noun_1", "verb_1", "verb_2", "verb_3", "verb_4", "noun_5", "place", "noun_6", "noun_7", "place_2", "verb_6", "food_2", "game", "verb_7", "noun_8", "noun_9", "plural_noun", "plural_noun", "ing_verb", "verb_8", "plural_noun_2", "verb_9", "noun_1", "noun_1", "food_1"],
    """If you give a {animal} a {food_1}, he is going to as for a {noun_1}. When you give him the {noun_1}, he will want to {verb_1}. When he is finished, he will {verb_2}. Then he will {verb_3} and {verb_4} to the {noun_5}. Since that doesn't work out, he will want to go to {place}. 
    On the way, he will see a {noun_6} and will want {noun_7}. The you will have to take him to the {place_2}. He will {verb_6}. When he is done, he will ask you for some {food_2}. On the way home he will start a game of {game}. When you finally get home, you'll have to {verb_7}. Then he will want a {noun_8}. You'll have to find a {noun_9} and {plural_noun}. When he sees the {plural_noun}, he will start {ing_verb}.
    Then he will {verb_8} out of {plural_noun_2}. Of course, when he is finished he will want to {verb_9}. So, he will ask for a {noun_1}. And, chances are, if you give him a {noun_1}, he is going to want a {food_1}."""
)

story2 = Story(
    "omg",
    "Amusement Parks",
    ["noun_1", "article_of_clothing", "adjective_1", "adjective_2", "noun_2", "plural_noun_1", "noun_3", "adjective_3", "type_of_food", "type_of_liquid", "body_part", "plural_noun_2", "plural_noun_3", "animal", "noun_4"],
    """An amusement park is always fun to visit on a hot summer {noun_1}. When you get there, you can wear your {article_of_clothing} and go for a swim. And there are lots of {adjective_1} things to eat. You can start of with a/an {adjective_2}-dog on a/an {noun_2} with mustard, relish, and {plural_noun_1} on it. Then you can have a buttered ear of {noun_3} with a nice {adjective_3} slice of {type_of_food} and a big bottle of cold {type_of_liquid}. When you are full, it's time to go ona rollercoaster, which should settle your {body_part}. Other amusement park rides are the bumper cars, which have little {plural_noun_2} that you drive and run into other {plural_noun_3}, and the merry-go-round, where you can sit on a big {animal} and try to grab the gold {noun_4} as you ride past it."""
)

story3 = Story(
    "wow",
    "Road Trip",
    ['adjective_1', 'place', 'adjective_2', 'adjective_3', 'plural_noun_1', 'plural_noun_2', 'noun_1', 'verb_1', 'noun_2', 'ed_verb', 'action_verb_1', 'plural_noun_3', 'noun_3', 'ing_verb', 'noun_4', 'time_measurement', 'adjective_4', 'action_verb_2', 'verb_2', 'adjective_5', 'possessive_noun'],
    """On the {adjective_1} trip to {place}, my {adjective_2} friend and I decided to invent a game. Since this would be a rather {adjective_3} trip, it would need to be a game with {plural_noun_1} and {plural_noun_2}. Using our {noun_1} to {verb_1}, we tried to get the {noun_2} next to us to play too, but they just {ed_verb} at us and {action_verb_1} away. After a few rounds, we thought the game could use some {plural_noun_3} so we turned on the {noun_3} and started {ing_verb} to the {noun_4} that came on. This lasted for {time_measurement} before I got {adjective_4} and decided to {action_verb_2}. I'll never {verb_2} that trip, it was the {adjective_5} road trip of my {possessive_noun}."""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3]}

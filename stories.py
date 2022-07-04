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
    ["animal", "food", "noun", "last_noun", "verb", "verb", "verb", "verb", "noun", "place", "noun", "noun", "place", "verb", "food", "game", "verb", "noun", "noun", "plural_noun", "last_noun", "ing_verb", "verb", "plural_noun", "verb", "first_noun", "first_noun", "first_food"],
    """If you give a {animal} a {food}, he is going to as for a {noun}. When you give him the {last_noun}, he will want to {verb}. When he is finished, he will {verb}. They he will {verb} and {verb} to the {noun}. Since that doesn't work out, he will want to go to {place}. 
    On the way, he will see a {noun} and will want {noun}. The you eull have to take him to the {place}. He will {verb}. When he is done, he will ask you for some {food}. On the way home he will start a game of {game}. When you finally get home, you'll have to {verb}. Then he will want a {noun}. You'll have to find a {noun} and {plural_noun}. When he sees the {last_noun}, he will start {ing_verb}.
    Then he will {verb} out of {plural_noun}. Of course, when he is finished he will want to {verb}. So, he will ask for a {first_noun}. And, chances are, if you give him a {first_noun}, he is going to want a {first_food}."""
)

story2 = Story(
    "omg",
    "Amusement Parks",
    ["noun", "article_of_clothing", "adjective", "adjective", "noun", "plural_noun", "noun", "adjective", "type_of_food", "type_of_liquid", "body_part", "plural_noun", "plural_noun", "animal", "noun"],
    """An amusement park is always fun to visit on a hot summer {noun}. When you get there, you can wear your {article_of_clothing} and go for a swim. And there are lots of {adjective} things to eat. You can start of with a/an {adjective}-dog on a/an {noun} with mustard, relish, and {plural_noun} on it. Then you can have a buttered ear of {noun} with a nice {adjective} slice of {type_of_food} and a big bottle of cold {type_of_liquid}. When you are full, it's time to go ona rollercoaster, which should settle your {body_part}. Other amusement park rides are the bumper cars, which have little {plural_noun} that you drive and run into other {plural_noun}, and the merry-go-round, where you can sit on a big {animal} and try to grab the gold {noun} as you ride past it."""
)

story3 = Story(
    "wow",
    "Road Trip",
    ['adjective', 'place', 'adjective', 'adjective', 'plural_noun', 'plural_noun', 'noun', 'verb', 'noun', 'verb', 'action_verb', 'plural_noun', 'noun', 'ing_verb', 'noun', 'time_measurement', 'adjective', 'action_verb', 'verb', 'adjective', 'possessive_noun'],
    """On the {adjective} trip to {place}, my {adjective} friend and I decided to invent a game. Since this would be a rather {adjective} trip, it would need to be a game with {plural_noun} and {plural_noun}. Using our {noun} to {verb}, we tried to get the {noun} next to us to play too, but they just {verb}ed at us and {action_verb} away. After a few rounds, we thought the game could use some {plural_noun} so we turned on the {noun} and started {ing_verb} to the {noun} that came on. This lasted for {time_measurement} before I got {adjective} and decided to {action_verb}. I'll never {verb} that trip, it was the {adjective} road trip of my {possessive_noun}."""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3]}

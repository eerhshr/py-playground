import random

activity_list = [
    'Make a flower bouquet',
    'Paint a picture',
    'DIY wall frame',
    'Gardening',
    'Go for a walk',
    'Bake a dessert',
    'LEGO time',
    'Try making pasta from scratch',
    'Play your keyboard',
    'Hike day',
    'Try a new coffee shop',
    'SPA Day',
    'Watercolor painting',
    'Golf Day',
    'Solve a Puzzle',
    'Get a mini Crochet kit',
    'Try pottery',
    'Sip and paint',
    'Calligraphy',
    'Try Candle Making',
    'Learn an unique origami',
    'Learn to make jam or pickle',
    'Read a book',
    'Learn basics for personal finance',
    'Digital Declutter',
    'Research the culture and history of an era/place',
    'Bake bread',
    'Watch an old classic movie',
    'Volunteer from home',
    'Try designing on Canva',
    'Knit a scarf',
    'Edit a picture',
    'Organize your closet',
    'Try a new recipie',
    'Play arcade games',
]


def activity_generator():
    activity_picked = random.choice(activity_list)
    return activity_picked

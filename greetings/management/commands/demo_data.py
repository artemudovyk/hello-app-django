from django.core.management.base import BaseCommand, CommandError
from ...models import Greeting

demo_marvel_names = [
    'Captain.America@marvel.com',
    'Ironman@marvel.com',
    'Thor@marvel.com',
    'Hulk@marvel.com',
    'Spider-Man@marvel.com',
    'Wolverine@marvel.com',
    'Deadpool@marvel.com',
    'Daredevil@marvel.com',
    'Doctor.Strange@marvel.com',
    'Black.Panther@marvel.com',
    'Professor.X@marvel.com',
    'Magneto@marvel.com',
    'Star-Lord@marvel.com',
    'Ghost.Rider@marvel.com',
    'Thing@marvel.com',
    'War.Machine@marvel.com',
    'Drax.the.Destroyer@marvel.com',
    'Bucky.Winter.Soldier@marvel.com',
    'Hawkeye@marvel.com',
    'Nightcrawler@marvel.com',
    'Silver.Surfer@marvel.com',
    'Thanos@marvel.com',
    'Human.Torch@marvel.com',
    'Taskmaster@marvel.com',
    'Quicksilver@marvel.com',
    'Venom@marvel.com',
    'Jessica.Jones@marvel.com',
    'Storm@marvel.com',
    'Rogue@marvel.com',
    'Invisible.Woman@marvel.com',
    'Doctor.Doom@marvel.com',
    'Jean.Grey@marvel.com',
    'Norman.Osborn@marvel.com',
    'Red.Skull@marvel.com',
    'Mr.Fantastic@marvel.com',
    'Sabertooth@marvel.com',
    'Gambit@marvel.com',
    'Nick.Fury@marvel.com',
    'Colossus@marvel.com',
    'Cyclops@marvel.com',
    'Loki@marvel.com',
    'Beast@marvel.com',
    'Black.Window@marvel.com',
    'Vision@marvel.com',
    'The.Punisher@marvel.com',
    'Luke.Cage@marvel.com',
    'Iceman@marvel.com',
    'Groot@marvel.com',
    'Scarlet.Witch@marvel.com',
    'Rocket.Raccoon@marvel.com',
    'Cable@marvel.com',
    'Ms.Marvel@marvel.com',
    'X-23@marvel.com',
    'Ant-Man@marvel.com',
    'Wasp@marvel.com',
    'Valkyrie@marvel.com',
    'Pepper.Potts@marvel.com',
    'Ronan.the.Accuser@marvel.com',
    'Modok@marvel.com',
    'Abomination@marvel.com',
    'Lady.Deathstrike@marvel.com',
    'Ultron@marvel.com',
    'Wilson.Fisk@marvel.com',
    'Doctor.Octopus@marvel.com',
    'Apocalypse@marvel.com',
    'Kang@marvel.com',
    'Mandarin@marvel.com',
    'Mystique@marvel.com',
    'Sebastian.Shaw@marvel.com',
    'Blade@marvel.com',
    'Emma.Frost@marvel.com',
    'Justin.Hammer@marvel.com',
    'Surtur@marvel.com',
    'William.Stryker@marvel.com',
    'Elektra@marvel.com',
    'Purple.Man@marvel.com',
    'Mister.Immortal@marvel.com',
    'Galactus@marvel.com',
    'Dormammu@marvel.com',
    'The.Beyonder@marvel.com',
    'Phoenix.Force@marvel.com',
    'Thane@marvel.com',
    'Captain.Marvel@marvel.com',
    'Domino@marvel.com',
    'Enchantress@marvel.com',
    'Carnage@marvel.com',
    'J.Jonah.Jameson@marvel.com',
    'Angel@marvel.com',
    'Falcon@marvel.com',
    'Juggernaut@marvel.com',
    'Squirrel.girl@marvel.com',
    'Yondu.Udonta@marvel.com',
    'Mary.Jane.Watson@marvel.com',
    'Howard.the.Duck@marvel.com',
    'Iron.Fist@marvel.com',
    'Agent.Phil.Coulson@marvel.com',
    'Moon.Knight@marvel.com',
    'Cloak.and.Dagger@marvel.com',
    'Nebula@marvel.com',
    'Bullseye@marvel.com',
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        objs = []
        for email in demo_marvel_names:
            new_greeting = Greeting(email=email)
            objs.append(new_greeting)
            
        Greeting.objects.bulk_create(objs)
            
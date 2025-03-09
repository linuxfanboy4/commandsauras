import random
import time
import sys
import os

dinosaur_jokes = [
    "Why can't you hear a pterodactyl go to the bathroom? Because the 'P' is silent!",
    "Why don't dinosaurs ever use cell phones? Because they're all extinct!",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
    "What do you call a sleeping dinosaur? A dino-snore!",
    "Why was the T-Rex always angry? Because he couldn't reach the top shelf!"
]

dinosaur_commands = {
    "ls": lambda: print(random.choice(dinosaur_jokes)),
    "sudo": lambda: print("Sudo? You mean 'SO DO!' Get it? Because... you know... 'SO' enthusiastically!"),
    "dinosaur": lambda: print("A giant beast from ancient times, they roamed the Earth, and left us with fossilized memories."),
    "whoami": lambda: print("You are a human, but now you're a Time-Traveling Dino Enthusiast!"),
    "dinohelp": lambda: print("Available Commands: ls, sudo, dinosaur, whoami, joke, dino-facts, dino-quote, fossilize, time-travel, dig, and many more!"),
    "joke": lambda: print(random.choice(dinosaur_jokes)),
    "dino-facts": lambda: print("Dinosaurs existed for over 165 million years, and they came in all sizes, from tiny chicken-sized dinosaurs to giant 100+ ton beasts."),
    "dino-quote": lambda: print("The only thing we have to fear is... not having enough fossils! - A famous paleontologist"),
    "fossilize": lambda: print("You are now a fossil! Just kidding, but you're as cool as one."),
    "time-travel": lambda: print("You're in the Mesozoic Era now, enjoy the time travel! Watch out for that T-Rex!"),
    "dig": lambda: print("You dig around and uncover a fossilized dino claw. Looks like a T-Rex's..."),
    "eat": lambda: print("You try to eat a leaf... wait, wrong era! You're supposed to be a carnivore or herbivore depending on the dino you are!"),
    "sleep": lambda: print("You curl up like a little raptor... Zzzzz..."),
    "run": lambda: print("You run... but a Velociraptor is chasing you! Faster!"),
    "swim": lambda: print("You're in the water like a Plesiosaurus, gracefully swimming with ease."),
    "fly": lambda: print("You spread your wings like a Pteranodon and soar through the skies!"),
    "roar": lambda: print("ROAAAR! You're a mighty T-Rex! The Earth trembles beneath your roar!"),
    "dance": lambda: print("You attempt to dance, but you end up looking like a dinosaur trying to moonwalk."),
    "dino-dance": lambda: print("The Velociraptors show you their signature dance moves, you're impressed!"),
    "hunt": lambda: print("You hunt like a predator... oh no! You were hunted by a bigger dinosaur!"),
    "saurus-simulator": lambda: print("You simulate being a dinosaur in a prehistoric world. Life is hard, but you're surviving!"),
    "dino-meme": lambda: print("Why did the T-Rex break up with his girlfriend? She was dino-saurious!"),
    "extinct": lambda: print("Your dinosaur species went extinct millions of years ago. But don't worry, you're back now!"),
    "fossil-hunter": lambda: print("You find an ancient fossil, maybe a Stegosaurus? The excitement is real!"),
    "t-rex-challenge": lambda: print("The T-Rex challenge! Try to get something off the top shelf. Too bad your arms are too short!"),
    "t-rex-roar": lambda: print("You unleash a deafening T-Rex roar, shaking the ground beneath you!"),
    "volcano-eruption": lambda: print("A volcanic eruption is happening nearby! Quick, run!"),
    "dino-craft": lambda: print("You craft a primitive stone tool. A dinosaur's gotta survive!")
}

unix_commands = {
    "pwd": lambda: print(f"/home/dino/prehistoric/{random.choice(['jurassic', 'cretaceous', 'triassic', 'mesozoic'])}"),
    "cd": lambda: print("You try to travel through time, but this is a prehistoric system! You can't just `cd` anywhere."),
    "cat": lambda: print("You try to `cat` a file... but all you get are ancient fossils."),
    "echo": lambda: print("RAWR! This is your dinosaur echo!"),
    "touch": lambda: print("You try to `touch` something... but it's a fossil. Can't touch the past, can you?"),
    "cp": lambda: print("You copy your favorite fossil. Now you have two T-Rex skulls."),
    "mv": lambda: print("You move your collection of dinosaur bones around. A real paleontologist's day job."),
    "rm": lambda: print("You attempt to remove a dino bone... but it’s way too heavy!"),
    "man": lambda: print("The `man` command? We only have dino experts here, not manuals! Try `dinohelp` instead."),
    "top": lambda: print("You look at the top of the food chain, and it's you... or maybe that giant T-Rex."),
    "df": lambda: print("Disk space in prehistoric times? The Earth was your hard drive!"),
    "ps": lambda: print("Process list: T-Rex (eating), Velociraptor (running), Pteranodon (flying)."),
    "kill": lambda: print("You can't kill a dinosaur... but it’s a fun thought, right?"),
    "history": lambda: print("History of dinosaurs: Roamed Earth for 165 million years, and then... extinction."),
    "alias": lambda: print("You alias yourself as 'T-Rex' and now, you're the king of the command line!"),
    "clear": lambda: print("You clear the command line... but the prehistoric world remains."),
    "chmod": lambda: print("You chmod your fossil collection, but it remains unbreakable."),
    "find": lambda: print("You search for the lost city of dinosaurs, but it’s lost... just like their history."),
    "man": lambda: print("Man pages? Try `dinohelp` to learn about the prehistoric world."),
    "tail": lambda: print("You look at the tail of a Stegosaurus. It's massive!"),
    "head": lambda: print("You look at the head of a T-Rex... it's looking at you, too."),
    "grep": lambda: print("You search through ancient fossils with a magnifying glass, looking for clues."),
    "locate": lambda: print("You locate a dino nest... It's a Velociraptor's den!"),
    "find": lambda: print("You find an ancient fossil of a Triceratops buried in the sand."),
    "mkdir": lambda: print("You try to create a new directory, but it turns into a new dinosaur habitat."),
    "rmdir": lambda: print("You try to remove a directory, but it's full of dino bones!"),
    "nano": lambda: print("You try to `nano` a file, but all you get is ancient hieroglyphics."),
    "vim": lambda: print("You attempt to `vim` something, but it feels like you're writing the history of the dinosaurs."),
    "chmod": lambda: print("You chmod your fossil collection to 'read-only'. It's safe forever."),
    "ln": lambda: print("You link a fossil from one time period to another. Time travel at its best."),
    "cp -r": lambda: print("You recursively copy a fossil site. More fossils for you to study!"),
    "mv -f": lambda: print("You forcefully move a fossil, but it's too heavy! Time to get help from a dino."),
    "diff": lambda: print("You compare two dino fossils... they look almost identical, except for the teeth!"),
    "du": lambda: print("Disk usage in the dino world? Well, it's all in the bones... lots of them."),
}

def show_intro():
    print("""
 __  
               / _)  
      _.----._/ /  
     /          /  
 __/ (  | (  |  
/__.-'|_|--|_|  
    """)
    print("Hello! You're 160 million years back from your timeline.")

def handle_command(command):
    if command in dinosaur_commands:
        dinosaur_commands[command]()
    elif command in unix_commands:
        unix_commands[command]()
    else:
        print(f"Command '{command}' is not recognized. But hey, dinosaurs had the same issue. Try again!")

def escape_secret():
    secret_command = "RAWR!"
    while True:
        user_input = input("Type the secret command to escape: ")
        if user_input == secret_command:
            print("RAWR! You escaped the prehistoric command line!")
            sys.exit(0)
        else:
            print("Oops! Wrong secret command. Try again!")

def main():
    show_intro()
    while True:
        command = input("CommandSaurus> ").strip()
        if command == "exit":
            print("Haha, nice try! You can't exit this way. Try typing the secret command to escape.")
        elif command == "Ctrl+C":
            print("Nice try again! Dinosaurs never give up, and neither should you!")
        else:
            handle_command(command)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Nice try! You can't exit by pressing Ctrl + C, you're stuck in the Jurassic command world!")
        time.sleep(2)
        escape_secret()

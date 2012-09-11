from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from subprocess import Popen, PIPE
import random

SEKRIT = "This is a secret message!"

#  ls /usr/share/cowsay
#
#     (obscene cowfiles commented out :D)
#
cowfiles = (
        "beavis.zen",
        "bong",
        "bud-frogs",
        "bunny",
        "cheese",
        "cower",
        "daemon",
        "default",
        "dragon-and-cow",
        "dragon",
        "elephant-in-snake",
        "elephant",
        #"eyes",
        "flaming-sheep",
        "ghostbusters",
        "head-in",
        "hellokitty",
        "kiss",
        "kitty",
        "koala",
        "kosh",
        "luke-koala",
        "mech-and-cow",
        "meow",
        "milk",
        "moofasa",
        "moose",
        "mutilated",
        "ren",
        "satanic",
        "sheep",
        "skeleton",
        "small",
        #"sodomized",
        "stegosaurus",
        "stimpy",
        "supermilker",
        "surgery",
#         "telebears",
        "three-eyes",
        "turkey",
        "turtle",
        "tux",
        "udder",
        "vader-koala",
        "vader",
        "www"
        )

def index(request):

    cowsay  = __get_cowsay()
    cowfile = cowsay[0]
    stdout  = cowsay[1]

    t = loader.get_template('layout.html') 
    c = Context({
        'sekrit':SEKRIT,
        'cowfile': cowfile,
        'cowsay': stdout
    })

    return HttpResponse(t.render(c))


def __get_cowsay():
    wrapcolumn = '50'
    cowfile = cowfiles[random.randint(0, len(cowfiles))-1]

    cowsaycmd  = ['cowsay', '-W', wrapcolumn]
    cowsaycmd.extend(['-f', cowfile])

    # stick out a tongue 50% of the time
    #if random.randint(0,1) is 1:
    #   cowsaycmd.extend(['-T', 'U'])

    # see http://docs.python.org/library/subprocess.html#replacing-shell-pipeline
    fortunecmd = ['fortune']
    p1 = Popen(fortunecmd, stdout = PIPE)
    p2 = Popen(cowsaycmd, stdin=p1.stdout, stdout=PIPE)

    (stdout, stdin) = p2.communicate() 

    return (cowfile, stdout)


if __name__ == "__main__":
    print __get_cowsay()

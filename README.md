# bigs
Bipartite matching on complete graphs in Python.

## Setup
You will need to specify the ordered "preferences" of each participant. There are example `.pref` files in the `examples` directory.

### Partial Orders create Partial Solutions
If every participant in a given group (male and female) has a fully ordered ranking of every participant in the other group, then there is always at least one stable solution with a perfect matching such that:

1. every person is assigned a partner
2. no two partners would rather be with each other than with their current partners

If the ordering is not completely specified, then a stable matching is not guaranteed.

## Usage
The primary program to run is `match.py`, which implements the Gale-Shapely algorithm for solving the stable-marriage problem.

The problem is itself implemented as a `Graph` class in `graph.py`.

There are two input parameters to `match.py`, which specify the two input files of preferences.

Use the "`--help`" parameter to see the *Help* dialogue.

    $ > python match.py --help
    Usage: match.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -b MEN, --bachelors=MEN
      -p WOMEN, --houses=WOMEN

### How does it work?
In the Gale-Shapely algorithm implemented in this program, every "step" tries to determine, for some Romeo, which Juliet he should be assigned to. Based on his preferences, his current "best option Juliet" is picked and he goes over to her balcony to check her out. If she hasn't had any other suitors yet, then he hits the jackpot and gets automatically engaged to Ms. Juliet. 

If she already has at least one other suitor, however, then the two Romeos have to duel it out (and by that - I just mean that Juliet determines which one she would prefer and sends the other on his merry way). If the previous suitor (who I refer to as "Paris") is superior, then the new suitor is rejected and he must try the next Juliet on his list. If the previous suitor is dumped ("divorced"), then he returns to the list of eligible bachelor Romeos while the new suitor proposes to fair Juliet.

These shenanigans continue until there are no bachelor Romeos left. That is to say, either every Romeo has been assigned to his own Juliet, or every unmatched Romeo has attempted to propose to every Juliet, got rejected at each one, and there is no perfect solution.

**FUN MATH TIME!!**

As long as there are 2 groups of equal size N and each participant in each group creates a complete ranking of every member of the other group, then there is at least one perfect solution.

### "Perfect" does not imply "Perfection"
The biggest thing to take away, however, is that just because a solution is perfect "on-paper" does not mean that it is truly the optimal solution. There may be multiple perfect solutions, and there may be superior solutions that require adding more participants. 

"Perfect" only means that everybody got matched with somebody else. It is synonymous with "symmetric" in this case. It does not mean that everybody gets matched with their #1 pick. If there are 5 Juliets and 25 Romeos, and every selected Romeo/Juliet matching was between two participants who both rated each other #1 overall, then this is the ideal stable matching because everyone who got matched also got the one person they would never leave for anyone else. Unfortunately, it also leaves 20 Romeos without a match at all, but in some cases **this is ok**. 

### Order Matters
In the Gale-Shapely algorithm implemented in this program, the assignment of a group of participants to being "male" or "female" actually has quite a bit of importance. This isn't square-dancing. The apt analogy is, surprisingly enough, Romeo & Juliet. 

Juliet (women) are confined to a balcony, and cannot actively choose who to pursue. They can only decide, given a list of men trying to propose, who they would prefer out of the group.

Romeo (men) are always searching for the best possible match for themselves, and will sequentially try every balcony until they aren't rejected.

In this sense, each Juliet is matched to her favorite Romeo who *happened* to come to her balcony, while each Romeo is matched to his #1 ranked Juliet who is also the first Juliet willing to "settle" for him. Juliet's #1 favorite Romeo might never ever come to her balcony, but Romeo will try Juliet #1 then Juliet #2 then Juliet #3 and so on until he isn't rejected any more.

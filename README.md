<h1>Simple Variable-Size Rock, Paper, Scissors.</h1>

Basic RPS (rock, paper, scissors) is played by default. To play RPSLS (rock, paper,
scissors, lizard, spock) comment the current name_mappings, and uncomment the
game-specific one. You can also add your own options as long as the follow the input
rules below.

<b>Input Rules:</b>

This game, much like normal RPS, or its extension RPSLS, relies on the number of
options being odd in order for balance to be maintained. If this were not the case,
diferent options would have lower or higher chances of winning. The proof of this is
left up to the reader as an exercise.
Aside from this requirement of odd-ness, there are no specific game-related input rules,
however there are some semantic ones. Specifically, the key for each option must be
unique or the game will break. Lastly, the options must be input in order of their increasing
cyclical dominance. This will allow the code to dynamically determine all other dominances
and preserve cyclical dominance while running.

<b>Dominance Mapping:</b>

Dominance is decided based on the rules of RPS and its extension RPSLS. In these games,
each option has an equivalent number of options it dominates, and is dominated by (rock beats
scissors & paper beats rock) which, when summed, are equal to the total number of other options
available. For basic gameplay (RPS) there is only one unique solution for cyclical dominance which
is enough to maintain this requirement, but for higher dimensional gameplay (RPSLS), there exist
several unique solutions for cyclical dominance which are required for our rules to be satisfied.
Thus, we borrow the further dominance rules from the RPSLS model by maintaining that every option
dominates the option that dominates its dominator. More specifically, taking the subset of any
three options as nodes, we create a directed cyclic graph where edge direction denotes domination.
More simply, we create a game of RPS with each set of three options. In this way we are able to
fully generate our dominance map for any set of options.

Project 2
=========

A simulated TMTO-attack of car-key authentication system using Rainbow-tables.


## Content

 * `TableGenerator.py` - Script generating Rainbow-tables with given
   parameters and hardcoded `u`
 * `RainbowAttack.py` - Script using the Rainbow-table to crack
   hardcoded `u`


## Usage

`TableGenerator.py` creates a Rainbow-table with a hardcoded `u` and
parameters. The resulting table is printed to a cvs called `table.cvs`. It
is run with, simply:

    $ python TableGenerator.py
    
`RainbowAttack.py` uses the previously created Rainbow-table and
hardcoded `u` to search for a matching key `s`.

    $ python RainbowAttack.py


## Logic

With a generator table, the `RainbowAttack.py` script the following:

 1. The key broadcasts to car (in this case the **adversary**)
 2. The car/eve responds with a challenge `u`.
 3. The key then responds with a hash consisting of `MD5(s||u)`.
 4. Eve now uses the Rainbow-table to crack `s`.

Once this is done Eve can open the car at will.


## Further Help

For further help or explanation please contact one of us by mail and
we'll be happy to help:

 * Markus Faerevaag [s123692@student.dtu.dk](mailto:s123692@student.dtu.dk)
 * Christian Mathias Rohde Kiaer [s123812@student.dtu.dk](mailto:s123812@student.dtu.dk)
 * Jonathan Becktor [s123094@student.dtu.dk](mailto:s123094@student.dtu.dk)

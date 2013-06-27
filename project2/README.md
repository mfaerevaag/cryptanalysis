Project 2
=========

A simulated TMTO-attack of car-key authentication system using Rainbow-tables.


## Content

 * `TableGenerator.py` - Script generating Rainbow-tables with given
   parameters and hardcoded `u`
 * `RainbowAttack.py` - Script using the Rainbow-table to crack
   hardcoded `u`
 * `table.csv` - Rainbowtable generated from TableGenerator.py
 * `test.py` - Used to test the Rainbowtable as we had lots of problems with the generating the table.

*NOTE:* As we have discussed, our rainbowtable attack is not fully functional. We don't know why and what we are doing wrong, but the success rate is extremely low. We have testet our tables, and they are infact correct. Our only guess right now, is the computation of the respone r's successors is wrong or we have misunderstood how to do it.

## Attack idea

Our attacker is a person who tries to steal the car. He proceeds as follows:

 * He picks an arbitrary, fixed challenge u and precomputes a Rainbow Table for the function f(s) = lowest 28 bit of MD5(s||u).
 * When he gets access to a car key for a short time, he presses the button on the key fob. Then he acts on behalf of the car by sending a challenge u and receiving the response r.
 * He now uses his Rainbow Table to find a value s with f(s) = r.
 * He verifies this secret by sending some trial challenges to the key fob and checking whether he can compute the right response. If he can, then he has found the correct secret, meaning that he now can open the car at will.

## Rainbowtable attacks described

Rainbowtables are a time memory tradeoff attack, wich makes it possible to crack hashed passwords. Rainbowtables computes a table of m rows and t chains, only storing the random selected starting point and the computed end point. Each computation in the chain applies a reduction function on the hashed values.

The reduction functions of a rainbow table are all different (one per column), but are generally built as an extension of a single reduction function.

In our example we use the reduction function f(s) = (s + 1) % BITSIZE.  

## Usage

`TableGenerator.py` creates a Rainbow-table with a hardcoded `u` and
parameters. The resulting table is printed to a cvs called `table.cvs`. It
is run with, simply:

    $ python TableGenerator.py

The generated table should now contain 2^18 rows and with the chains included around 2^28 covered points(this will be lower, cause of collisions).
    
`RainbowAttack.py` uses the previously created Rainbow-table and
hardcoded `u` to search for a matching key `s`.

    $ python RainbowAttack.py

RainbowAttack computes all the successor of a response r (computed from the given equations), and checks if any of these successors is in the loaded table. If a successor is equal to an endpoint, this row will be used to compute the password. The startpoint of the table is used to compute the chain of reduction functions. If one of these functions matches r, the value before should be the password. This is not 100% certain, as the could be in the table without the key being there.

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

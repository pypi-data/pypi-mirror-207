# Tennis Library


The Tennis library is a Python package that provides functionalities for simulating tennis matches and tiebreakers. It offers easy-to-use methods to simulate and track scores, tiebreakers, and various statistics. The tennis library is perfect for tracking real time data input.

<br><br>
## Features

The Tennis library offers the following main features:
<br><br>
### 1. Match Simulation

The match simulation feature allows you to simulate a full tennis match between two players. It will automatically keep track of match stats and comply with complicated rules like tiebreakers, AD, and serving
<br><br>
### 2. Tiebreaker

The tiebreaker feature enables you to simulate a tiebreakerIt provides an easy-to-use interface for conducting tiebreakers, scoring points, and tracking statistics.
<br><br>
### Tracking Stats

Both the match simulation and tiebreaker features include built-in mechanisms for tracking various statistics. These statistics include:

- Aces
- Double faults
- First serve percentage
- First serve points won
- Second serve percentage
- Second serve points won
- Serve games won
- Return games won
- Winners
- Unforced errors
- Points won by volley
- Points won by dropshot
- Points won by overhead

These statistics help analyze player performance and provide insights into the gameplay.


<br><br>
## Usage

To use the Tennis library, follow these steps:

1. Install the library by running <br> `pip install tennis`.
   <br><br>
2. import libraries<br>
```python
from tennis import match

from tennis import tiebreak
```



<br>
Here's an example of how to simulate a tennis match using the Tennis library:

```python
from tennis import match

# create a new match instance
a = match.TennisMatch("a","b",{"num_games_to_win":6, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})

# call win_point() player "a" won the point by an "overhead, opponent unforced error, and a dropshot"
a.win_point("a", ["overhead"])
a.win_point("a",['unforced_errors'])
a.win_point("a", ["win_by_dropshot"])

# gets a string representation of the scoreboard. Player "a" score will be displayed on top
print(a.get_scoreboard("a"))

# gets a string representation of the stats. Player "a" will be displayed on the left
print(a.print_stats("a"))

```

output: 
```
╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    0  0  40   *                a
    0  0  0                    b

╚═════════════════════════════════════╝


════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
```



<br><br><br>

Here's an example of how to simulate a tennis tiebreak using the Tennis library:

```python
from tennis import tiebreak

#create a new tiebreak instance
tb = tiebreak.tiebreak("a","b",{"first_to_num_points":7, "win_by":2, "whos_serve":"a"})

#player "a" wins the point
tiebreak.win_point("a")

#player "b" misses a first serve
tiebreak.serve_fault("b")

#returns a string representation of the scoreboard
print(tiebreak.get_scoreboard("a"))

```

output:
```
╔═════════════════════════════════════╗
            Tiebreak Score

     T
     1                   a
     0  *                b

╚═════════════════════════════════════╝



════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
```

<br><br><br>
## **Useful Methods**
```python

match.backup_data()
```


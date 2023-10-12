This code solves the October 2023 "Coins" challenge from DMCommunity.org

It uses the python-constraint library from https://pypi.org/project/python-constraint/

First output with time instrumentation (time.process_time()):
4563 solutions in 182 ms

The average time across 1,000 trials was 191 ms on an i-7 notebook.

The solutions returned are not number of coins but total value for each denomination, which allows using the ExactSumConstraint and minimizes multiplication.
These solutions can be turned back into "count of coins" solutions by dividing each pile value by the value of the coin.

RushHour Solver
***************

Tool for parsing and solving Rush Hour boards.

**Components**

* Cli
* Board Parser
* Rush Hour Solver
* Rush Hour Painter

Installation
============

Rush Hour Solver can be installed as a local pip package.

Simply run:

    .. code-block:: bash

        $ pip install -e ./path/to/rushhour-solver

Commands
========

The Rush Hour Solver Cli module is for supplying a manual control
interface.

for the default function based on a correct demo board,
simply run without arguments:

    .. code-block:: bash

        $ rush [OPTIONS] [FILENAME]

**Options**

-l --log   Set logger output level.
--test     Run all Rush Hour tests.

Test coverage
=============

Test supplied for basic functions of the cli.



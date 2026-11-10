"""The trial record class of the installed Inspect Robots, under the name the tests use.

Inspect Robots 1.0 renamed ``TrialRecord`` to ``Record`` with no alias; 0.59 and 0.60 have only
``TrialRecord``. The tests build records directly, so they take the class from here.
"""

import inspect_robots

TrialRecord = getattr(inspect_robots, "Record", None) or inspect_robots.TrialRecord

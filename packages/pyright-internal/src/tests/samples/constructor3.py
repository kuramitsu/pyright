# This sample tests inference of constructed types (in this case,
# for "chain") when the expected type is provided by another
# constructor (in this case "list").

# pyright: strict

from concurrent.futures import Future, wait
from itertools import chain
from typing import Any, Dict, Literal

my_list = list(chain([0]))
t1: Literal["list[int]"] = reveal_type(my_list)


pending: Dict[Future[Any], Any] = {}
done_tasks, _ = wait(list(pending.keys()))

t2: Literal["Set[Future[Any]]"] = reveal_type(done_tasks)

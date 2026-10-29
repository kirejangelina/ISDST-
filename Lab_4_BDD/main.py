def push(queue: list[str], msg: str) -> None:
    queue.append(msg)


def pop(queue: list[str]) -> str:
    if not queue:
        raise IndexError("pop from empty queue")
    return queue.pop(0)


def peek(queue: list[str]) -> str:
    if not queue:
        raise IndexError("peek from empty queue")
    return queue[0]


def is_empty(queue: list[str]) -> bool:
    return len(queue) == 0

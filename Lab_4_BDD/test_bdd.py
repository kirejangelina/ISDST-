import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from main import push, pop, peek, is_empty

scenarios('features/queue.feature')


@pytest.fixture
def queue():
    return []


@given("пустая очередь")
def empty_queue(queue):
    # Очередь уже создана пустой в фикстуре
    assert is_empty(queue)


@given(parsers.parse('очередь с сообщениями "{msg1}", "{msg2}", "{msg3}"'))
def queue_with_messages(queue, msg1, msg2, msg3):
    push(queue, msg1)
    push(queue, msg2)
    push(queue, msg3)


@when("я добавляю сообщение \"{message}\"")
def add_message(queue, message):
    push(queue, message)


@when("я извлекаю сообщение")
def extract_message(queue):
    global extracted_msg
    extracted_msg = pop(queue)


@then("очередь должна быть пустой")
def check_is_empty(queue):
    assert is_empty(queue)


@then("очередь не должна быть пустой")
def check_not_empty(queue):
    assert not is_empty(queue)


@then("при попытке извлечь сообщение возникает ошибка")
def check_pop_error(queue):
    with pytest.raises(IndexError):
        pop(queue)


@then("следующим сообщением будет \"{msg}\"")
def check_peek(queue, msg):
    assert peek(queue) == msg


@then("извлеченным сообщением будет \"{msg}\"")
def check_extracted(queue, msg):
    global extracted_msg
    assert extracted_msg == msg


@then("первым в очереди останется \"{msg}\"")
def check_next_in_queue(queue, msg):
    assert peek(queue) == msg

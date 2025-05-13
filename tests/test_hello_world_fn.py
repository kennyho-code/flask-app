from flaskr.hello_world_fn import hello_world_fn


def test_hello_world_fn():
    assert hello_world_fn() == "hello world"

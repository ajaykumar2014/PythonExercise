import uuid


def say():
    print('This is module 1')


UUID = uuid.uuid4()

PROJECT = 'GCP10001-232432342'


class Utils:
    uuid: str = UUID

    def test(name: str) -> str:
        print(f'VVVV{uuid}')
        print(f'{name}-{type(name)}-{uuid.uuid4()}')

    def test1(name: str = UUID) -> str:
        return name

    def test2(name: str = UUID, location: str = PROJECT) -> str:
        return f'{location}---{UUID}'

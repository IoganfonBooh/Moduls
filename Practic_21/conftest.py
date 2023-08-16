import pytest
import datetime
from datetime import datetime
@pytest.fixture(autouse=True)

def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"

def test_request_1(request_fixture):
    print(request_fixture)

class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)
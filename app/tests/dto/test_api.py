import random
import unittest

from module.api.dto.request import *
from module.api.dto.response import *
from module.api.exception import EmptyList


class TestDTOApiPart(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        pass

    def test_api_dto_request_time(self):
        value = random.randint(1, 100000000)
        token = random.randint(100000001, 200000000)
        self.assertEqual({'action': value, 'token': token}, ServerTimeDTOApiRequest(value, token))
        self.assertNotEqual({'action': value - 1, 'token': token}, ServerTimeDTOApiRequest(value, token))
        self.assertNotEqual({'action': value, 'token': token - 1}, ServerTimeDTOApiRequest(value, token))

    def test_api_dto_response_time(self):
        dto = ServerTimeDTOApiResponse()

        # Multiple test
        tests = self.generator_dto_response_time()

        with self.assertRaises(EmptyList):
            dto.export()

        for item in tests:
            (datetime_str, action_str, token) = item
            self.assertEqual({'datetime': datetime_str, 'action': action_str},
                             dto.export({'datetime_app': datetime_str, 'action_app': action_str, 'token_app': token}))

    @staticmethod
    def generator_dto_response_time():
        value1 = random.randint(1, 100000000)
        value2 = random.randint(100000001, 200000000)
        value3 = random.randint(200000001, 300000001)

        yield value1, value2, value3
        yield value1, None, value3
        yield None, None, value3
        yield None, value2, value3
        yield value1, value2, None

    def test_api_dto_response_status(self):
        dto = StatusDTOApiResponse()

        # Multiple test
        tests = self.generator_dto_response_status()

        with self.assertRaises(EmptyList):
            dto.export()

        for item in tests:
            (token, status) = item
            self.assertEqual({'status': status}, dto.export({'token_app': token, 'status_app': status}))

    @staticmethod
    def generator_dto_response_status():
        value = random.randint(1, 100000000)
        yield value, True
        yield value - 1, False
        yield None, True


if __name__ == '__main__':
    unittest.main()

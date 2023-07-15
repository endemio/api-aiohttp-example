import random
import unittest

from module.application.dto.request import *
from module.application.dto.response import *


class TestDTOApplicationPart(unittest.TestCase):

    # execute before every test case function run.
    def setUp(self):
        pass

    def test_api_dto_request_time(self):
        value = random.randint(1, 100000000)
        self.assertEqual([value, ''], ServerTimeDTOAppRequest({'action': value}))
        self.assertNotEqual({'action': value - 1}, ServerTimeDTOAppRequest({'action': value}))

    def test_api_dto_response_time(self):
        # Multiple test
        tests = self.generator_dto_response_time()

        for item in tests:
            (datetime_str, action_str) = item
            self.assertEqual(
                {
                    'datetime_app': datetime_str if datetime_str else '',
                    'action_app': action_str if action_str else ''
                },
                ServerTimeDTOAppResponse(test=123, datetime=datetime_str, fake=222, action=action_str))

    @staticmethod
    def generator_dto_response_time():
        value1 = random.randint(1, 100000000)
        value2 = random.randint(100000001, 200000000)

        yield value1, value2
        yield value1, None
        yield None, None
        yield None, value2
        yield value1, value2

    def test_api_dto_response_status(self):

        # Multiple test
        tests = self.generator_dto_response_status()

        for item in tests:
            (token, status) = item
            self.assertEqual({'status_app': status if status else False},
                             StatusDTOAppResponse(fake=333, status=status, test=123))

    @staticmethod
    def generator_dto_response_status():
        value = random.randint(1, 100000000)
        yield value, True
        yield value - 1, False
        yield None, None


if __name__ == '__main__':
    unittest.main()

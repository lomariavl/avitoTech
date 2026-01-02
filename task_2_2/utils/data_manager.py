import json
import logging
from pathlib import Path

from task_2_2.models.for_test_data import TestData


class DataManager:
    _TEST_DATA_PATH = Path(__file__).parent.parent.parent.joinpath('task_2_2', 'resources', 'test_data.json')

    @staticmethod
    def get_test_data() -> TestData:
        try:
            with open(DataManager._TEST_DATA_PATH) as file:
                data = json.load(file)
                test_data = TestData(**data)
                return test_data
        except FileNotFoundError:
            logging.error(f'Path does not exist: {DataManager._TEST_DATA_PATH}')
        except (json.JSONDecodeError, TypeError):
            logging.error(f'Invalid JSON on the path {DataManager._TEST_DATA_PATH}')

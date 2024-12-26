import logging
import unittest
from Runner_3 import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            peshehod = Runner('Пешеход', -5)
            for i in range(10):
                peshehod.walk()
            self.assertEqual(peshehod.distance, 60)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            begun = Runner(456378)
            for i in range(10):
                begun.run()
            self.assertEqual(begun.distance, 120)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                            exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
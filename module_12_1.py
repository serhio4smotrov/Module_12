import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('name')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner = Runner('name')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance,100)

    def test_challenge(self):
        runner1 = Runner('first')
        runner2 = Runner('second')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance,runner2.distance)
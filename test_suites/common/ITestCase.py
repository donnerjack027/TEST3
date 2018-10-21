from abc import abstractmethod


class ITestCase:

    def __init__(self):
        print(' ')

    @abstractmethod
    def test_run(self):
        """
        Method should be implemented in actual testcases

        :return:
        """
        return NotImplemented
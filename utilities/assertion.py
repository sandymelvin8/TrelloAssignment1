"""
This module contains Assertion related classes.
"""
import logging


class Assert(object):
    """
    This class is responsible for providing assertion mechanism for the test cases.
    Basic rule for assertion is to raise exception when assertion fails, and do nothing when is passed
    """

    @staticmethod
    def assert_true(condition, error_message):
        """
        Assert on the given condition.
        If condition is false, raise exception, do nothing otherwise

        :param condition: condition to evaluate
        :param error_message: error message to use when assertion fails
        """
        if not condition:
            logging.error("assert_true failed. Condition: " + str(condition))
            raise Exception(error_message)

    @staticmethod
    def assert_false(condition, error_message):
        """
        Assert false on the given condition.
        If condition is when True, raise exception, do nothing otherwise

        :param condition: condition to evaluate
        :param error_message: error message to use when assertion fails
        """
        if condition:
            logging.error("assert_false failed. Condition: " + str(condition))
            raise Exception(error_message)

    @staticmethod
    def assert_equals(expected, actual, error_message):
        """
        Check if expected and actual are equal.
        This works for string, number and list

        :param expected: expected value
        :param actual: actual value
        :param error_message: error message to use when comparison fails
        """
        if expected != actual:
            logging.error("Assert Equal failed.\nExpected:\n" + str(expected) + "\nActual:\n" + str(actual))
            raise Exception(error_message)

    @staticmethod
    def assert_fails(error_message):
        """
        Fails the test
        :param error_message: error message to use
        """
        raise Exception(error_message)

    @staticmethod
    def assert_not_equals(expected, actual, error_message):
        """
        Check if expected and actual are not equal.
        This works for string, number and list

        :param expected: expected value
        :param actual: actual value
        :param error_message: error message to use when comparison fails
        """
        if expected == actual:
            logging.error("assert_not_equal failed. Expected: " + str(expected) + ", Actual: " + str(actual))
            raise Exception(error_message)

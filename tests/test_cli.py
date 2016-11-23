# -*- coding: utf-8 -*-

"""
Module: tests
File: test_cli.py
Creator: Nick Geense
Date: 23-11-2016

Unit Tests for Rush Hour CLI.

"""


import unittest
from unittest.mock import patch
import logging

from click.testing import CliRunner

from rushhour_solver import cli


class TestRushHourCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

        patcher_subprocess = patch('rushhour_solver.cli.subprocess.run')
        self.mock_subprocess = patcher_subprocess.start()
        self.addCleanup(patcher_subprocess.stop)

    def test_cli(self):
        result = self.runner.invoke(cli.main)
        self.assertFalse(result.exception)
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Trying to find a solution..', result.output.strip())

    def test_cli_with_option_log(self):
        result = self.runner.invoke(cli.main, ['--log=info'])
        loglevel = logging.getLogger().getEffectiveLevel()

        self.assertFalse(result.exception)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(loglevel, logging.INFO)

    def test_cli_option_test(self):
        result = self.runner.invoke(cli.main, ['--test'])
        self.assertEqual(self.mock_subprocess.call_count, 1)


if __name__ == '__main__':
    unittest.main()


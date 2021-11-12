# -*- coding: utf-8 -*-


import unittest
import unittest.mock as mock

import ckunlock.dbunlock
import ckunlock.cksession


class DbUnlockTest(unittest.TestCase):

    def test_unlock_session(self):
        self.assertEqual(ckunlock.dbunlock.unlock_session('foo'),
                         'dbus-send --system --print-reply --dest="org.freedesktop.ConsoleKit"' + \
                         ' /org/freedesktop/ConsoleKit/foo org.freedesktop.ConsoleKit.Session.Unlock')

    def test_unlock_users(self):
        with mock.patch('subprocess.call') as mock_call:
            mock_call.return_value = 0
            with mock.patch('ckunlock.cksession.CkSession') as mock_cksession:
                mock_cksession.return_value = mock.MagicMock(name='cksession-mock')
                mock_cksession.list_sessions.return_value = mock_cksession
                mock_cksession.x11_session.return_value = 'foobar'
                self.assertEqual(ckunlock.dbunlock.unlock_users('bar'), 0)


class CkSessionTest(unittest.TestCase):

    def one(self):
        pass

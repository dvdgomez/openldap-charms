# Copyright 2022 Dave
# See LICENSE file for licensing details.

import unittest

import ops.testing
from ops.model import ActiveStatus
from ops.testing import Harness

from charm import HpctLdapServerCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        # Enable more accurate simulation of container networking.
        # For more information, see https://juju.is/docs/sdk/testing#heading--simulate-can-connect
        ops.testing.SIMULATE_CAN_CONNECT = True
        self.addCleanup(setattr, ops.testing, "SIMULATE_CAN_CONNECT", False)

        self.harness = Harness(HpctLdapServerCharm)
        self.addCleanup(self.harness.cleanup)

    def test_start(self):
        # Simulate the charm starting
        self.harness.begin_with_initial_hooks()

        # Ensure we set an ActiveStatus with no message
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())

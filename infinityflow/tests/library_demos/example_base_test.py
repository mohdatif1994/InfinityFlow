"""Example Base Test"""
from __future__ import annotations

import sys

from infinityflow.src.lib.core.basetest import BaseTest


class ExampleBaseTestUsage(BaseTest):
    """Class to Test Base Test"""

    def setup(self):
        """Setup"""
        self._log.error("In Setup")
        return super().setup()

    def execute(self):
        """Execute"""
        self._log.info("In execute")
        return super().execute()

    def cleanup(self):
        """Cleanup"""
        self._log.info("In cleanup")
        return super().cleanup()


if __name__ == "__main__":
    sys.exit(B.main(B))

"""Example exception"""
import sys
from infinityflow.src.lib.core.basetest import BaseTest

class B(BaseTest):
    """B Class"""
    def setup(self):
        """Setup"""
        self._log.error("In Setup")
        return super(B, self).setup()
    
    def execute(self):
        """Execute"""
        self._log.info("In execute")
        return super(B, self).execute()
    
    def cleanup(self):
        """Cleanup"""
        self._log.info("In cleanup")
        return super(B, self).cleanup() 

if __name__ == "__main__":
    sys.exit(B.main(B))
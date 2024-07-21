import sys
from infinityflow.src.lib.core.basetest import BaseTest

class B(BaseTest):

    def setup(self):
        self._log.error("In Setup")
        return super(B, self).setup()
    
    def execute(self):
        self._log.info("In execute")
        return super(B, self).execute()
    
    def cleanup(self):
        self._log.info("In cleanup")
        return super(B, self).cleanup() 

if __name__ == "__main__":
    sys.exit(B.main(B))
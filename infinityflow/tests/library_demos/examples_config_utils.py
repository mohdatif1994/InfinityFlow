from infinityflow.src.lib.core.config import Config

obj = Config('/Users/mohdatifkhan/Desktop/testing_branch/InfinityFlow/InfinityFlow/infinityflow/src/config/config.yaml')
cfg = obj.get_cfg_opts()
print(cfg)

print(Config.get_logging_cfg(cfg))

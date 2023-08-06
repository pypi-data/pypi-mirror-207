import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parents[2])
sys.path.append(ROOT)

from trademasterntu.collector.builder import COLLECTORS
from trademasterntu.collector.custom import CollectorBase

@COLLECTORS.register_module()
class BinanceRealTimeDataCollector(CollectorBase):
    def __init__(self):
        super(BinanceRealTimeDataCollector, self).__init__()

    def run(self):
        pass
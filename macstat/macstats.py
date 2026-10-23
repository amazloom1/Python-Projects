import rumps
import psutil
from collections import namedtuple

Stats = namedtuple("Stats", ["cpu", "memory"])

def get_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return Stats(cpu=cpu, memory=mem)

class macstats(rumps.App):
    def __init__(self):
        super().__init__("macstats")
        psutil.cpu_percent()
        
        self.title = "CPU --% | MEM --%"

        self.timer = rumps.Timer(self.update, 1)
        self.timer.start()

    def update(self, sender):
        stats = get_stats()
        fs = "\u2007"  # figure space: same width as a digit

        cpu = f"{stats.cpu:.0f}".rjust(3, fs)
        mem = f"{stats.memory:.0f}".rjust(3, fs)

        self.title = f"CPU{cpu}% | MEM{mem}%"
        self._nsapp.nsstatusitem.setLength_(150)

if __name__ == "__main__":
    macstats().run()

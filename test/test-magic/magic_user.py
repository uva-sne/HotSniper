# Monitor SimMarker() calls made by the application.

import sim
class Marker:
  def setup(self, args):
    args = (args or '').split(':')
    self.write_terminal = 'verbose' in args
    self.write_markers = 'markers' in args
    self.write_stats = 'stats' in args

  def hook_magic_marker(self, thread, core, a, b, s):
    print '[SCRIPT] My own Magic marker from thread %d: a = %d' % (thread, a)

sim.util.register(Marker())


# Register the user commands that we can call from the benchmark

def hook_magic_user(core, a):
  print '[SCRIPT] Magic user from core %d: a = %d' % (core, a)
  print 'Time:[t=%3dus]' % (sim.stats.time() / 1e9),
  return 0

def hook_magic_user2(core, a):
  print '[SCRIPT] Magic user2 from core %d: a = %d' % (core, a)
  current_time = sim.stats.time()
  print 'Time:[t=%3dus]' % (current_time / 1e9),
  return current_time


sim.util.register_command(0x123, hook_magic_user)
sim.util.register_command(0x124, hook_magic_user2)

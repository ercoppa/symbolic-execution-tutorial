import angr, logging
import claripy
import pdb
import resource
import time

proj = angr.Project('bomb.exe')

start = 0x401190 # initial state is at the beginning of phase_one()
avoid = [0x401960]
end = [0x4011AD]

state = proj.factory.blank_state(addr=start)

# a symbolic input string with a length up to 128 bytes
arg = state.se.BVS("input_string", 8 * 128)
# an ending byte
arg_end = state.se.BVS("end_input_string", 8)
state.se.add(arg_end == 0x0) # add a constraint on this byte to force it to be '\0'
# the constraint is added to the state.
# Another way to do same is with:
#   arg_end = state.se.BVV(0x0, 8)
# in this case arg_end is a concrete value

# concat arg and arg_end
arg = state.se.Concat(arg, arg_end)

# an address where to store my arg
bind_addr = 0x603780

# bind the symbolic string at this address
state.memory.store(bind_addr, arg)

state.stack_push(state.se.BVV(bind_addr, 32))
state.stack_push(state.se.BVV(0x0, 32))

pg = proj.factory.simulation_manager(state)

start_time = time.time()
while len(pg.active) > 0:

    print pg

    # step 1 basic block for each active path
    pg.explore(avoid=avoid, find=end, n=1)

    # Bazinga!
    if len(pg.found) > 0:
        print
    	print "Reached the target"
        print pg
        state = pg.found[0].state
        print "Solution: " + state.se.eval(arg, cast_to=str)
        break

print
print "Memory usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + " MB"
print "Elapsed time: " + str(time.time() - start_time)

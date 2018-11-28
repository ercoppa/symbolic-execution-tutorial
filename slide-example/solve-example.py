import angr

proj = angr.Project('example')

# customize XXX, YYY, and ZZZ!!!
start = XXX    # addr of foobar
avoid = [YYY]  # point(s) that are not interesting (e.g., early exits)
end = ZZZ      # point that I want to reach

# blank_state since exploration should start from an arbitrary point
# otherwise, use entry_state()
state = proj.factory.blank_state(addr=start)

# arguments are inside registers in x86_64
a = state.regs.edi
b = state.regs.esi

sm = proj.factory.simulation_manager(state)

while len(sm.active) > 0:

    print sm # get a feeling of what is happening
    sm.explore(avoid=avoid, find=end, n=1)

    if len(sm.found) > 0: # Bazinga!
        print "\nReached the target\n"
        state = sm.found[0].state
        print "%edi = " + str(state.se.eval_upto(a, 10))
        print "%esi = " + str(state.se.eval_upto(b, 10))
        break

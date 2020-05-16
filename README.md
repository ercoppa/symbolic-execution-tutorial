# Symbolic Execution

## Slides

Current version of the slides is available [here](https://docs.google.com/presentation/d/e/2PACX-1vR7ZG-wQu9SvGA2wv7GFn2pLU9z3N_yAfoqiHRgn5I3RU-9k9XTEsjdKHZBUshau3TBY1fLZe2vnHmx/pub?start=false&loop=false&delayms=3000).

Download slides:
* revision 2020-05-16: [PDF](symbolic-execution-2020-05-16.pdf)
* revision 2019-12-05: [PDF](symbolic-execution-2018-12-05.pdf)
* revision 2018-11-29: [PDF](symbolic-execution-2018-11-29.pdf)

## Hands-on

### Setup

See [setup/README.md](setup/README.md).

### Slide example

You can find the source code, binary (Linux x86_64) and an angr script in the `slide-example` directory. `solve-example.py` ***must*** be customized, replacing {XXX, YYY, ZZZ} placeholders.

### Logic bomb

A Windows PE-32 logic bomb can be found in the `bomb/` directory. A very similar bomb for Linux/x86_64 can be found in the `linux-bomb/` directory.
Source code is not available. The angr script for solving the first phase is called `phase-1.py` (replace {XXX, YYY, ZZZ} placeholders!).

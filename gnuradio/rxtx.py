#!/usr/bin/env python2

# Activate two python flow graphs as built by grc

import dttsprx
import dttsptx

def main():
    tbrx = dttsprx.dttsprx()
    tbrx.start()
    tbtx = dttsptx.dttsptx()
    tbtx.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tbrx.stop()
    tbtx.stop()
    tbrx.wait()
    tbtx.wait()


if __name__ == '__main__':
    main()

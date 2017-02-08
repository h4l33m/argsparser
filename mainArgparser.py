#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
 
def main():
    parser = argparse.ArgumentParser()
 
    parser.add_argument('condition',
                    metavar='CONDITION',
                    type=str,
                    help='Choose : star or stop,
                    choices=['yes', 'no'])
                
    parser.add_argument('path',
                    metavar=' FILE PATH',
                    type=str,
                    help='Enter Path')
 
    args = parser.parse_args()
    operation = args.operation
    path = args.path
 
    if operation == 'start':
        print("It start here %s" %path)
    elif operation == 'stop':
        print("Stoping %s" %path )
    sys.exit(0)
 
if __name__ == '__main__':
    main()
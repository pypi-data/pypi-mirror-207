#!/usr/bin/env python3
"""
Read values from the Keithley DMM6500.
"""

import argparse
import sys

from mmcb import common
from mmcb import dmm_interface


##############################################################################
# command line option handler
##############################################################################


def check_arguments(settings):
    """
    handle command line options

    --------------------------------------------------------------------------
    args
        settings : dictionary
            contains core information about the test environment
    --------------------------------------------------------------------------
    returns : none
    --------------------------------------------------------------------------
    """
    parser = argparse.ArgumentParser(
        description='Reads voltage or current from the Keithley DMM6500.'
    )

    parser.add_argument(
        '-c', '--current',
        action='store_true',
        help='Read current (A)')
    parser.add_argument(
        '-v', '--voltage',
        action='store_true',
        help='Read voltage (V)')

    args = parser.parse_args()

    if args.current:
        settings['current'] = args.current

    if args.voltage:
        settings['voltage'] = args.voltage


##############################################################################
# main
##############################################################################


def main():
    """ set the voltage on a power supply connected by RS232 """

    settings = {}
    check_arguments(settings)

    dmm = dmm_interface.Dmm6500()
    configure = {
        'current': dmm.configure_read_current,
        'voltage': dmm.configure_read_voltage,
    }

    for function, required in settings.items():
        if not required:
            continue

        configure[function]()
        value = dmm.read_value()
        print(f'{function}, {common.si_prefix(value)}, {value}')


##############################################################################
if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
Read values from the Keithley DMM6500.
"""

import argparse
import sys
import time

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
        '-c', '--capacitance',
        action='store_true',
        help='Read capacitance (F)')
    parser.add_argument(
        '--currentac',
        action='store_true',
        help='Read AC current (A)')
    parser.add_argument(
        '-i', '--currentdc',
        action='store_true',
        help='Read DC current (A)')
    parser.add_argument(
        '-r', '--resistance',
        action='store_true',
        help='Read two-wire resistance (\u03a9)')
    parser.add_argument(
        '-t', '--temperature',
        action='store_true',
        help='Read temperature (\u00b0C)')
    parser.add_argument(
        '--voltageac',
        action='store_true',
        help='Read AC voltage (V)')
    parser.add_argument(
        '-v', '--voltagedc',
        action='store_true',
        help='Read DC voltage (V)')

    args = parser.parse_args()

    if args.capacitance:
        settings['capacitance'] = args.capacitance
    if args.currentac:
        settings['currentac'] = args.currentac
    if args.currentdc:
        settings['currentdc'] = args.currentdc
    if args.resistance:
        settings['resistance'] = args.resistance
    if args.temperature:
        settings['temperature'] = args.temperature
    if args.voltageac:
        settings['voltageac'] = args.voltageac
    if args.voltagedc:
        settings['voltagedc'] = args.voltagedc


##############################################################################
# main
##############################################################################


def main():
    """ set the voltage on a power supply connected by RS232 """

    settings = {}
    check_arguments(settings)

    dmm = dmm_interface.Dmm6500()
    configure = {
            'capacitance': dmm.configure_read_capacitance,
            'currentac': dmm.configure_read_ac_current,
            'currentdc': dmm.configure_read_dc_current,
            'resistance': dmm.configure_read_resistance,
            'temperature': dmm.configure_read_temperature,
            'voltagedc': dmm.configure_read_dc_voltage,
            'voltageac': dmm.configure_read_ac_voltage,
    }

    # AC quantities sometimes return None on the first attempt
    retries = 3

    for function, required in settings.items():
        if not required:
            continue

        configure[function]()

        for _ in range(retries):
            value = dmm.read_value()
            if value is not None:
                break
            time.sleep(0.1)

        if value > 9e+37:
            print(f'{function}, overflow, overflow')
        else:
            print(f'{function}, {common.si_prefix(value)}, {value}')


##############################################################################
if __name__ == '__main__':
    sys.exit(main())

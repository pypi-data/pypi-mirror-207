#!/usr/bin/env python3
"""
Read values from the Keithley DMM6500.
"""

import argparse
import sys
import threading
import time

import serial

from mmcb import common
from mmcb import lexicon


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
# set psu values
##############################################################################

def read_voltage(pipeline, ser, dev):
    """
    Read the voltage as measured at the output terminals.

    --------------------------------------------------------------------------
    args
        pipeline : instance of class Production
            contains all the queues through which the production pipeline
            processes communicate
        ser : serial.Serial
            reference for serial port
        dev : instance of class Channel
            contains details of a device and its serial port
    --------------------------------------------------------------------------
    returns
        measured_voltage : float or None
    --------------------------------------------------------------------------
    """
    command_string = lexicon.instrument(dev.model, 'set up to read voltage')
    common.send_command(pipeline, ser, dev, command_string)

    time.sleep(0.1)

    command_string = lexicon.instrument(dev.model, 'read value')
    response = common.atomic_send_command_read_response(pipeline, ser, dev, command_string)

    try:
        value = float(response)
    except ValueError:
        value = None

    return value


def read_current(pipeline, ser, dev):
    """
    Read the current as measured at the output terminals.

    --------------------------------------------------------------------------
    args
        pipeline : instance of class Production
            contains all the queues through which the production pipeline
            processes communicate
        ser : serial.Serial
            reference for serial port
        dev : instance of class Channel
            contains details of a device and its serial port
    --------------------------------------------------------------------------
    returns
        value : float or None
    --------------------------------------------------------------------------
    """
    command_string = lexicon.instrument(dev.model, 'set up to read current')
    common.send_command(pipeline, ser, dev, command_string)

    time.sleep(0.1)

    command_string = lexicon.instrument(dev.model, 'read value')
    response = common.atomic_send_command_read_response(pipeline, ser, dev, command_string)

    try:
        value = float(response)
    except ValueError:
        value = None

    return value


##############################################################################
# main
##############################################################################

def main():
    """ set the voltage on a power supply connected by RS232 """
    settings = {
        'current': None,
        'voltage': None,
    }

    check_arguments(settings)

    ##########################################################################
    # filter power supplies from cache leaving just a single channel
    ##########################################################################

    instruments = common.cache_read(['instrument'])

    channels = []
    for port, details in instruments.items():
        (config, device_type, serial_number, model,
         manufacturer, psu_channels, release_delay) = details

        for channel in psu_channels:
            channels.append(
                common.Channel(
                    port, config, serial_number, model, manufacturer, channel,
                    device_type, release_delay, None,
                )
            )

    ##########################################################################
    # set up resources for threads
    #
    # this is overkill since only one power supply channel will be used
    # but does allow the same well-tested interface employed by other scripts
    # in the suite to be used
    ##########################################################################

    class Production:
        """ Locks to support threaded operation. """
        portaccess = {
            port: threading.Lock()
            for port in {channel.port for channel in channels}
        }

    pipeline = Production()

    ##########################################################################
    # display details of selected power supply
    ##########################################################################

    try:
        channel = channels[0]
    except IndexError:
        pass
    else:
        operation = {'current': read_current, 'voltage': read_voltage}

        with serial.Serial(port=channel.port) as ser:
            ser.apply_settings(channel.config)
            ser.reset_input_buffer()
            ser.reset_output_buffer()

            for setting_name, execute in settings.items():
                if execute:
                    value = operation[setting_name](pipeline, ser, channel)
                    print(f'{setting_name}, {common.si_prefix(value)}, {value}')


##############################################################################
if __name__ == '__main__':
    sys.exit(main())

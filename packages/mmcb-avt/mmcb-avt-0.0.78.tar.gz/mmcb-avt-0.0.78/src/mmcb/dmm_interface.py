"""
Read values from the Keithley DMM6500.

https://docs.python.org/3.6/library/weakref.html#comparing-finalizers-with-del-methods
"""

import threading
import weakref

import serial

from mmcb import common
from mmcb import lexicon


##############################################################################
# data structures
##############################################################################


class Production:
    """
    Lock to support threaded operation in underlying library code
    """

    def __init__(self, channels):
        self.portaccess = {
            port: threading.Lock() for port in {channel.port for channel in channels}
        }


class Dmm6500:
    """
    Connection and reading from Keithley DMM 6500.
    """

    instruments = common.cache_read(['instrument'])

    channels = []
    for port, details in instruments.items():
        (
            config,
            device_type,
            serial_number,
            model,
            manufacturer,
            device_channels,
            release_delay,
        ) = details

        for channel in device_channels:
            channels.append(
                common.Channel(
                    port,
                    config,
                    serial_number,
                    model,
                    manufacturer,
                    channel,
                    device_type,
                    release_delay,
                    None,
                )
            )

    pipeline = Production(channels)

    try:
        channel = channels[0]
    except IndexError:
        pass

    def __init__(self):
        self.ser = serial.Serial(port=self.channel.port)
        self._finalizer = weakref.finalize(self, self.ser.close)
        self.ser.apply_settings(self.channel.config)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def remove(self):
        """manual garbage collection: close serial port"""
        self._finalizer()

    @property
    def removed(self):
        """check (indirectly) if the serial port has been closed"""
        return not self._finalizer.alive

    def configure_read_current(self):
        """
        Read the current as measured at the output terminals.

        --------------------------------------------------------------------------
        args : none
        --------------------------------------------------------------------------
        returns
            value : float or None
        --------------------------------------------------------------------------
        """
        common.send_command(
            self.pipeline,
            self.ser,
            self.channel,
            lexicon.instrument(self.channel.model, 'configure to read current'),
        )

    def configure_read_voltage(self):
        """
        Read the voltage as measured at the output terminals.

        --------------------------------------------------------------------------
        args : none
        --------------------------------------------------------------------------
        returns
            value : float or None
        --------------------------------------------------------------------------
        """
        common.send_command(
            self.pipeline,
            self.ser,
            self.channel,
            lexicon.instrument(self.channel.model, 'configure to read voltage'),
        )

    def read_value(self):
        """
        Read the voltage as measured at the output terminals.

        --------------------------------------------------------------------------
        args : none
        --------------------------------------------------------------------------
        returns
            value : float or None
        --------------------------------------------------------------------------
        """
        response = common.atomic_send_command_read_response(
            self.pipeline,
            self.ser,
            self.channel,
            lexicon.instrument(self.channel.model, 'read value'),
        )

        try:
            value = float(response)
        except ValueError:
            value = None

        return value

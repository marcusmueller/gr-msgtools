#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Marcus Müller.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import pmt

class msg_file_sink(gr.sync_block):
    """
    take a message and write it to a file as raw bytes of the message payload.
    """
    _in_port = pmt.intern("msg")
    def __init__(self, fname):
        gr.sync_block.__init__(self,
            name="msg_file_sink",
            in_sig=None,
            out_sig=None)
        self._file = open(fname, "w")
        self.message_port_register_in(self._in_port)
        self.set_msg_handler(self._in_port, self._msg_handler)

    def _msg_handler(self, msg):
        self._file.write(pmt.serialize_str(msg))


    def work(self, input_items, output_items):
        in0 = input_items[0]
        ##THIS CAN NEVER BE CALLED
        return len(input_items[0])


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 Marcus Müller.
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

from gnuradio import gr
import pmt
from pmt import pmt_to_python

class variable_to_msg(gr.basic_block):
    """
    When the set_value(value) method is called, sends a message containing a PMT dict {key, value}
    """

    _out_port = pmt.intern("out")

    def __init__(self, key):
        gr.basic_block.__init__(self,
            name="variable_to_msg",
            in_sig=[],
            out_sig=[])
        self._key = pmt.intern(key)
        self.message_port_register_out(self._out_port)

    def set_value(self, value, conversion = pmt.from_double ):
        """
        When the set_value(value) method is called, sends a message containing a PMT dict {key, value}
        """
        pmt_val = conversion(value)
        pmt_dict = pmt.make_dict()
        pmt_dict = pmt.dict_add(pmt_dict, self._key, pmt_val)
        self.message_port_pub(self._out_port, pmt_dict)




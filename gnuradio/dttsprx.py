#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dttsprx
# Generated: Sun Jan 24 18:33:44 2016
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class dttsprx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Dttsprx")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8000000

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/48000), firdes.low_pass(
        	1, samp_rate, 48000, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_interleaved_char_to_complex_0 = blocks.interleaved_char_to_complex(False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/tmp/iqdata", False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_sink_0 = audio.sink(48000, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 1), (self.audio_sink_0, 1))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_interleaved_char_to_complex_0, 0))    
        self.connect((self.blocks_interleaved_char_to_complex_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_float_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 48000, 1000, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=dttsprx, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()

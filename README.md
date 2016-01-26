# dttsp-sdr
Tools for turning dttsp into a complete sdr

HackRF transmit and receive with dttsp

I've gotten dttsp to transmit and receive through a HackRF by modifying
the hackrf_transfer program, now called hackrf_rxtx, and using GNU Radio
for rate conversion from 8mhz on the hackrf to 48khz with jack.

* dttsprx.grc and dttsprx.py
Receive from HackRF and downsample to 48khz using a FIR filter.
* dttsptx.grc and dttsptx.py
Transmit to a HackRF using the Rational Resampler.
* rxtx.py
Start both dttsprx and dttsptx

The .grc files are to be used with gnuradio-companion.

I start rxtx.py then the hackrf utility:

* ./hackrf_rxtx -r /tmp/iqdata -t /tmp/txiq -f 144292977 -s 8000000 -a 0 -l 40 -g 20 -x 47 -u 19004

* jack_connect sdr-tx:ol gr_source:in1; jack_connect sdr-tx:or gr_source:in0;jack_connect gr_sink:out0 sdr:ir; jack_connect gr_sink:out1 sdr:il



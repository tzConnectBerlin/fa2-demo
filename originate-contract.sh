#!/bin/sh


tezos-client -E http://granada.newby.org:8732 originate contract fa2-demo transferring 0 from florence running fa2.tz --init "`cat storage.tz`" --burn-cap 1.6375 --force

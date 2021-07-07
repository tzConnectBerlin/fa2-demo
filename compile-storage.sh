#!/bin/sh

cd smart-contracts

ligo compile-storage fa2_hooks/ligo/src/fa2_multi_asset.mligo multi_asset_main "`cat ../storage.mligo`" > storage.tz

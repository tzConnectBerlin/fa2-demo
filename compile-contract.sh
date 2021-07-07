#!/bin/sh
cd smart-contracts

ligo compile-contract fa2_hooks/ligo/src/fa2_multi_asset.mligo multi_asset_main > fa2.tz

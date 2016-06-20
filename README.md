# CAIDA Data Processing Scripts

This repository contains scripts to process CAIDA data.

`roots.py` takes an [AS
relationships](http://www.caida.org/data/as-relationships/) file and prints out
the list of roots, defined as those ASes that are not inferred to be customers
of any other AS.

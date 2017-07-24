#!/usr/bin/env bash
export PYTHONPATH="/home/jtmoulia/cupie:$PYTHONPATH"
temp="$(python -m cupie.therm)"
echo "Temperature (deg F): ${temp}"

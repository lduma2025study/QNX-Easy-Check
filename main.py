
# Build and Run Instructions

## QNX Version
QNX 8.0 (QNX Everywhere)

## Target Hardware
QEMU x86_64

## Toolchain
QNX SDP 8.0 - qcc compiler

## How to Build
1. Install QNX SDP 8.0
2. Run this host tool to generate build files:
   python main.py
3. Build the QNX app:
   make -f Makefile.qnx

## How to Run
Run on QEMU:
qemu-system-x86_64 -kernel my_qnx_app -m 512

## Host Tool
This project is a host tool. It runs on Windows, macOS and Linux.
It generates real QNX 8.0 build files: Makefile.qnx and main.c
main.c uses QNX Neutrino headers: <sys/neutrino.h>

## Category
Developer Tooling & Host Tools - QNX Global Hackathon

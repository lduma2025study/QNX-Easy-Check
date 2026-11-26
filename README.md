# QNX Easy-Check

A simple host tool for Windows, macOS and Linux that helps beginners check if their code is ready for QNX 8.0.

## Problem
Building for QNX 8.0 is hard for beginners. They don't know if their project is ready.

## Solution
QNX Easy-Check scans your project folder and checks:
1. README.md exists with build and run instructions
2. LICENSE file exists
3. Code files exist (.c, .cpp, .py)
4. README mentions QNX 8.0

It gives a simple report: PASS or FIX.

## How to Run
1. Download this repo
2. Open terminal
3. Run: python main.py
4. Type . for current folder

## Example Output
[PASS] README.md found
[PASS] LICENSE found
[PASS] Code files found
[PASS] README mentions QNX 8.0
Result: 4/4 - READY FOR QNX 8.0!

## Category
Developer Tooling & Host Tools - QNX Global Hackathon

## Built With
Python

## Team
Built by iduma2025study

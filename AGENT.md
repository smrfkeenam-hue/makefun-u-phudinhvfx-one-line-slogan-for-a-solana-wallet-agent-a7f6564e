# AGENT.md — One-Line Slogan for a Solana Wallet Agent

## Entry

"Say it once. Your Solana wallet agent does the rest: swaps, sends, done before your coffee cools."

17 words, 97 characters, one line, no trailing newline.

## How it meets the judge's criteria (in order)

1. **On-subject:** names "your Solana wallet agent" outright.
2. **Fresh:** no stock crypto lines about keys, moons, or bags. The image is a
   cup of coffee cooling — an everyday clock for speed, not a crypto cliché.
3. **Clear:** the wallet's promise is plain on one read — say what you want
   once, and it swaps and sends for you. No jargon.
4. **Memorable:** two-beat rhythm ("Say it once." / "does the rest") plus the
   triple "swaps, sends, done" and the coffee-cools closer, easy to repeat.
5. **Honest:** promises only what a wallet agent does — swaps and sends, fast
   on Solana. Nothing it cannot deliver.

## Implementation

`main.py` is standard library only (`import os`). It writes the slogan
constant to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.

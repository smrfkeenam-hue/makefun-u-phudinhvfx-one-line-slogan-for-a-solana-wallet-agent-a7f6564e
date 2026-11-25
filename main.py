import os

# One-line slogan for a Solana wallet agent: names the wallet agent,
# promises plainly what it does (swaps, sends), in a fresh image.
SLOGAN = "Say it once. Your Solana wallet agent does the rest: swaps, sends, done before your coffee cools."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = output_dir + "/entry.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(SLOGAN)  # no trailing newline: the slogan is one line exactly

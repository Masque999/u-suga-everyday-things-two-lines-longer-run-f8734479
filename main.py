LINES = [
    "A toaster is a tiny sunbed for bread: it lies under glowing hot wires until it turns golden brown on both sides.",
    "The sunbed comparison works because both use heat and time to change colour, but it leaves out that bread has no choice about when to get up.",
]

# The entry must be exactly two lines, 1-400 characters in total.
TEXT = "\n".join(LINES)
assert 1 <= len(TEXT) <= 400, f"text is {len(TEXT)} chars"
assert TEXT.count("\n") == 1

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == TEXT, "entry.txt does not match TEXT after write"

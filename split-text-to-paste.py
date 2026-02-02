import pyperclip

# Read from clipboard
text = pyperclip.paste()

# Split, clean, normalize
lines = [
    item.strip().upper()
    for item in text.split("|")
    if item.strip()
]

# Join with newlines (Excel rows)
output = "\n".join(lines)

# Write back to clipboard
pyperclip.copy(output)

print(f"Copied {len(lines)} items to clipboard.")

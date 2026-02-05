print("Enter your multiline text. Type 'END' on a new line to finish:")
lines = []
while True:
    line = input()
    if line == 'END':
        break
    lines.append(line)
    multiline_text = "\n".join(lines)
print("\n Your input:")
print(multiline_text)
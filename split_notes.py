import os

source = "complete_notes.tex"
with open(source, "r", encoding="utf-8") as f:
    lines = f.readlines()

def find_line(pattern, lines, start_line=0):
    for i in range(start_line, len(lines)):
        if pattern in lines[i]:
            return i
    return -1

idxs = {}
idxs['ch1'] = find_line(r"\section{Chapter 1", lines)
idxs['ch2'] = find_line(r"\section{Chapter 2", lines)
# Heuristic for Ch3 since header is missing
idxs['ch3'] = find_line("This document covers the principles of creating websites", lines)
idxs['ch4'] = find_line(r"\section{Chapter 4", lines)
idxs['ch5'] = find_line(r"\section{Chapter 5", lines)
idxs['ch6'] = find_line(r"\section{Chapter 6", lines)
idxs['ch7'] = find_line(r"\section{Chapter 7", lines)
idxs['ch8'] = find_line(r"\section{Chapter 8", lines)
idxs['ch9'] = find_line(r"\section{Chapter 9", lines)
idxs['mcq'] = find_line(r"\input{qa_fragments/mcq}", lines)

if idxs['mcq'] == -1:
    idxs['mcq'] = len(lines) - 2 # Fallback near end

print("Detected Indices:", idxs)

os.makedirs("chapters", exist_ok=True)

chapters = [
    ('ch1_html', 'ch1', 'ch2'),
    ('ch2_css', 'ch2', 'ch3'),
    ('ch3_bootstrap', 'ch3', 'ch4'),
    ('ch4_js', 'ch4', 'ch5'),
    ('ch5_react', 'ch5', 'ch6'),
    ('ch6_express', 'ch6', 'ch7'),
    ('ch7_mongo', 'ch7', 'ch8'),
    ('ch8_node', 'ch8', 'ch9'),
    ('ch9_redux', 'ch9', 'mcq')
]

for filename, start_key, end_key in chapters:
    s = idxs[start_key]
    e = idxs[end_key]
    
    if s == -1 or e == -1:
        print(f"Skipping {filename} due to missing index: {s} to {e}")
        continue

    chunk = lines[s:e]
    content = "".join(chunk)
    
    # Remove \newpage from the chunk to clean it up
    content = content.replace(r"\newpage", "")
    
    # Fix Ch3 missing header
    if start_key == 'ch3':
        content = "\\section{Chapter 3: Bootstrap & RWD}\n\n" + content

    with open(f"chapters/{filename}.tex", "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Written chapters/{filename}.tex")

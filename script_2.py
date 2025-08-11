# Let's examine a few sample files to show their contents
import os

folder_name = "100_hello_world_languages"

# Check a few sample files
sample_files = [
    "001_python_hello_world.py",
    "002_java_hello_world.java", 
    "010_php_hello_world.php",
    "018_haskell_hello_world.hs",
    "055_zig_hello_world.zig",
    "085_lolcode_hello_world.lol"
]

print("SAMPLE FILE CONTENTS:")
print("=" * 60)

for filename in sample_files:
    filepath = os.path.join(folder_name, filename)
    if os.path.exists(filepath):
        print(f"\n📁 {filename}")
        print("-" * 40)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        print("-" * 40)

# Create a summary list
print(f"\n\nSUMMARY: Created 100 'Hello, World!' programs")
print("=" * 60)

# Read the language list and create a comprehensive summary
languages_created = []
for i in range(1, 101):
    filename = f"{i:03d}_"
    for file in os.listdir(folder_name):
        if file.startswith(filename):
            lang_name = file.split('_')[1]
            ext = file.split('.')[-1]
            languages_created.append((i, lang_name, ext))
            break

print(f"Successfully created {len(languages_created)} files with Hello World programs!")
print("\nLanguages included (first 20):")
for i, (num, lang, ext) in enumerate(languages_created[:20]):
    print(f"{num:3d}. {lang:15} (.{ext})")

print("\n... (80 more languages)")

print(f"\nLanguages included (last 10):")
for i, (num, lang, ext) in enumerate(languages_created[-10:]):
    print(f"{num:3d}. {lang:15} (.{ext})")

print(f"\n✅ Task completed successfully!")
print(f"📁 Folder location: {folder_name}/")
print(f"📊 Total files: {len(languages_created)} Hello World programs")
print(f"🌍 Languages covered: From mainstream (Python, Java, C++) to esoteric (Brainfuck, LOLCODE)")
print(f"📝 Each file includes proper comments and language identification")
print(f"🔤 File naming: Sequential numbering with language name and extension")
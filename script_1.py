# Create folder and files for 100 "Hello World" programs
import os

# Take first 100 languages
selected_languages = hello_world_programs[:100]

# Create the main folder
folder_name = "100_hello_world_languages"
if os.path.exists(folder_name):
    import shutil
    shutil.rmtree(folder_name)

os.makedirs(folder_name)
print(f"Created folder: {folder_name}")

# Create files for each language
created_files = []
for i, (lang_name, file_ext, code) in enumerate(selected_languages, 1):
    filename = f"{i:03d}_{lang_name}_hello_world.{file_ext}"
    filepath = os.path.join(folder_name, filename)
    
    # Add a comment header to each file
    comment_chars = {
        'py': '#', 'java': '//', 'c': '//', 'cpp': '//', 'js': '//', 
        'cs': '//', 'go': '//', 'rs': '//', 'rb': '#', 'php': '//',
        'swift': '//', 'kt': '//', 'scala': '//', 'dart': '//', 'ts': '//',
        'pl': '#', 'lua': '--', 'hs': '--', 'erl': '%', 'ex': '#',
        'asm': ';', 'f90': '!', 'cob': '*>', 'pas': '{', 'adb': '--',
        'lisp': ';', 'scm': ';', 'clj': ';', 'fs': '//', 'ml': '(*',
        'html': '<!--', 'css': '/*', 'sh': '#', 'ps1': '#', 'bat': 'REM',
        'vbs': "'", 'sql': '--', 'xml': '<!--', 'json': '', 'yml': '#',
        'toml': '#', 'r': '#', 'm': '%', 'nb': '(*', 'jl': '#', 'tex': '%',
        'bf': '', 'ws': '', 'as': '//', 'alg': "'", 'apl': '⍝',
        'scpt': '--', 'ino': '//', 'awk': '#', 'bas': 'REM', 'bcpl': '//',
        'boo': '#', 'chpl': '//', 'icl': '//', 'clp': ';', 'coffee': '#',
        'curl': '{', 'dylan': '//', 'e': '--', 'elm': '--', 'ex': '--',
        'factor': '!', 'fal': '//', 'fs': '\\', 'gm': '//', 'groovy': '//',
        'hh': '//', 'icn': '#', 'idr': '--', 'inf': '!', 'io': '//',
        'ijs': 'NB.', 'lol': 'BTW', 'mod': '(*', 'oz': '%', 'pike': '//',
        'pro': '%', 'pb': ';', 'q': '/', 'rkt': ';', 'st': '"',
        'sml': '(*', 'tcl': '#', 'vala': '//', 'v': '//', 'vhdl': '--',
        'vb': "'", 'xsl': '<!--', 'xpath': '', 'ps': '%', 'mk': '#'
    }
    
    comment_char = comment_chars.get(file_ext, '#')
    
    # Create file content with header
    if comment_char and comment_char not in ['', '<!--', '(*', '{']:
        header = f"{comment_char} Hello World program in {lang_name.upper()}\n{comment_char} Language: {lang_name}\n{comment_char} File extension: .{file_ext}\n\n"
    elif comment_char == '<!--':
        header = f"<!-- Hello World program in {lang_name.upper()}\n     Language: {lang_name}\n     File extension: .{file_ext} -->\n\n"
    elif comment_char == '(*':
        header = f"(* Hello World program in {lang_name.upper()}\n   Language: {lang_name}\n   File extension: .{file_ext} *)\n\n"
    elif comment_char == '{':
        header = f"{{ Hello World program in {lang_name.upper()}\n  Language: {lang_name}\n  File extension: .{file_ext} }}\n\n"
    else:
        header = f"\nHello World program in {lang_name.upper()}\nLanguage: {lang_name}\nFile extension: .{file_ext}\n\n"
    
    full_content = header + code
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    created_files.append((filename, lang_name, file_ext))

print(f"\nSuccessfully created {len(created_files)} files!")
print(f"\nFirst 10 files created:")
for i, (filename, lang_name, ext) in enumerate(created_files[:10]):
    print(f"{i+1}. {filename}")

print(f"\nLast 10 files created:")
for i, (filename, lang_name, ext) in enumerate(created_files[-10:]):
    print(f"{i+91}. {filename}")

print(f"\nAll files are stored in the '{folder_name}' directory.")
print(f"Total files created: {len(created_files)}")

# Show folder contents
print(f"\nFolder contents preview:")
files_list = os.listdir(folder_name)
files_list.sort()
print(f"Total files in folder: {len(files_list)}")
print("Sample files:")
for i, f in enumerate(files_list[:5]):
    print(f"  {f}")
print("  ...")
for f in files_list[-3:]:
    print(f"  {f}")
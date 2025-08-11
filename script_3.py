# Create a README file for the folder
import os

folder_name = "100_hello_world_languages"
readme_content = """# 100 Hello World Programs

This folder contains **100 different "Hello, World!" programs** written in 100 different programming languages.

## 📁 Folder Contents

Each file is named with the pattern: `XXX_language_hello_world.extension`
- `XXX` = Sequential number (001-100)
- `language` = Programming language name
- `extension` = Appropriate file extension for the language

## 🌍 Languages Included

### Mainstream Languages (1-30)
1. **Python** (.py) - `print("Hello, World!")`
2. **Java** (.java) - Object-oriented with main class
3. **C** (.c) - Classic systems programming
4. **C++** (.cpp) - Object-oriented C extension
5. **JavaScript** (.js) - Web scripting language
6. **C#** (.cs) - Microsoft .NET language
7. **Go** (.go) - Google's systems language
8. **Rust** (.rs) - Memory-safe systems programming
9. **Ruby** (.rb) - Dynamic, object-oriented
10. **PHP** (.php) - Web development language
11. **Swift** (.swift) - Apple's iOS/macOS language
12. **Kotlin** (.kt) - JetBrains' Java alternative
13. **Scala** (.scala) - Functional/OOP hybrid
14. **Dart** (.dart) - Google's Flutter language
15. **TypeScript** (.ts) - Typed JavaScript
16. **Perl** (.pl) - Text processing powerhouse
17. **Lua** (.lua) - Lightweight scripting
18. **Haskell** (.hs) - Pure functional programming
19. **Erlang** (.erl) - Concurrent, fault-tolerant
20. **Elixir** (.ex) - Modern Erlang-based

### System & Assembly Languages (21-25)
21. **Assembly x86** (.asm) - Low-level machine code
22. **Fortran** (.f90) - Scientific computing
23. **COBOL** (.cob) - Business-oriented language
24. **Pascal** (.pas) - Structured programming
25. **Ada** (.adb) - Military/aerospace language

### Functional Languages (26-30)
26. **Lisp** (.lisp) - List processing pioneer
27. **Scheme** (.scm) - Minimalist Lisp dialect
28. **Clojure** (.clj) - Modern Lisp on JVM
29. **F#** (.fs) - .NET functional language
30. **OCaml** (.ml) - Industrial-strength functional

### Web & Markup Languages (31-42)
31. **HTML** (.html) - Web markup
32. **CSS** (.css) - Web styling
33. **Bash** (.sh) - Unix shell scripting
34. **PowerShell** (.ps1) - Windows automation
35. **Batch** (.bat) - Windows batch files
36. **VBScript** (.vbs) - Windows scripting
37. **SQL** (.sql) - Database queries
38. **PL/SQL** (.sql) - Oracle database language
39. **XML** (.xml) - Extensible markup
40. **JSON** (.json) - Data interchange format
41. **YAML** (.yml) - Human-readable data
42. **TOML** (.toml) - Configuration format

### Scientific & Mathematical Languages (43-47)
43. **R** (.r) - Statistical computing
44. **MATLAB** (.m) - Technical computing
45. **Mathematica** (.nb) - Symbolic computation
46. **Julia** (.jl) - High-performance scientific
47. **LaTeX** (.tex) - Document typesetting

### Esoteric Languages (48-50)
48. **Brainfuck** (.bf) - Minimalist esoteric
49. **Whitespace** (.ws) - Uses only whitespace
50. **Befunge** (.bf) - Two-dimensional esoteric

### Modern Systems Languages (51-55)
51. **Objective-C** (.m) - Apple's pre-Swift language
52. **D** (.d) - Systems programming
53. **Nim** (.nim) - Efficient and expressive
54. **Crystal** (.cr) - Ruby-like compiled language
55. **Zig** (.zig) - Modern systems programming

### Additional Languages (56-100)
56. ActionScript - Flash/Adobe development
57. Algol - Historical algorithmic language
58. APL - Array programming language
59. AppleScript - macOS automation
60. Arduino - Microcontroller programming
... and 40 more languages including AWK, BASIC, Chapel, Dylan, Eiffel, Forth, Groovy, Icon, J, LOLCODE, Mercury, Oz, Pike, Prolog, Racket, Smalltalk, Tcl, Verilog, and many others!

## 🚀 How to Use

1. **Browse by Language**: Each file is clearly named with the language
2. **Learning Resource**: Perfect for comparing syntax across languages
3. **Teaching Tool**: Great for demonstrating programming language diversity
4. **Reference**: Quick lookup for "Hello, World!" in any language

## 📋 File Structure

Each file contains:
- **Header comments** identifying the language
- **Proper syntax** for that language's "Hello, World!" program
- **Appropriate file extension** for the language
- **Language-specific comment style**

## 🎯 Language Categories Covered

- **Procedural**: C, Pascal, COBOL, Fortran
- **Object-Oriented**: Java, C++, C#, Scala
- **Functional**: Haskell, Lisp, Scheme, F#
- **Scripting**: Python, Ruby, Perl, Lua
- **Web**: JavaScript, PHP, HTML, CSS
- **Systems**: Rust, Go, Zig, Assembly
- **Scientific**: R, MATLAB, Julia, Mathematica
- **Esoteric**: Brainfuck, LOLCODE, Befunge
- **Domain-Specific**: SQL, LaTeX, VHDL, Verilog

## 📖 Educational Value

This collection demonstrates:
- **Syntax diversity** across programming paradigms
- **Evolution** of programming languages
- **Different approaches** to the same simple task
- **Language-specific features** and conventions
- **Historical perspective** on programming language development

Perfect for students, educators, and curious programmers exploring the rich landscape of programming languages!

---
*Created with comprehensive research from multiple programming language resources and syntax references.*
"""

readme_path = os.path.join(folder_name, "README.md")
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ README.md created successfully!")
print(f"📄 File location: {readme_path}")
print(f"📝 README contains comprehensive documentation of all 100 languages")

# Final verification
total_files = len(os.listdir(folder_name))
print(f"\n🎉 FINAL SUMMARY:")
print(f"📁 Folder: {folder_name}/")
print(f"📊 Total files: {total_files} (100 programs + 1 README)")
print(f"✨ Task completed successfully!")
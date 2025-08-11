import os

# Create a comprehensive list of 100 programming languages with Hello World programs
# Based on the extensive research from various sources

hello_world_programs = [
    # Popular mainstream languages
    ("python", "py", "print(\"Hello, World!\")"),
    ("java", "java", "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"),
    ("c", "c", "#include <stdio.h>\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}"),
    ("cpp", "cpp", "#include <iostream>\nusing namespace std;\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}"),
    ("javascript", "js", "console.log(\"Hello, World!\");"),
    ("csharp", "cs", "using System;\nclass HelloWorld {\n    static void Main() {\n        Console.WriteLine(\"Hello, World!\");\n    }\n}"),
    ("go", "go", "package main\nimport \"fmt\"\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}"),
    ("rust", "rs", "fn main() {\n    println!(\"Hello, World!\");\n}"),
    ("ruby", "rb", "puts \"Hello, World!\""),
    ("php", "php", "<?php\necho \"Hello, World!\";\n?>"),
    
    # Additional popular languages
    ("swift", "swift", "print(\"Hello, World!\")"),
    ("kotlin", "kt", "fun main() {\n    println(\"Hello, World!\")\n}"),
    ("scala", "scala", "object HelloWorld {\n    def main(args: Array[String]): Unit = {\n        println(\"Hello, World!\")\n    }\n}"),
    ("dart", "dart", "void main() {\n    print(\"Hello, World!\");\n}"),
    ("typescript", "ts", "console.log(\"Hello, World!\");"),
    ("perl", "pl", "print \"Hello, World!\\n\";"),
    ("lua", "lua", "print(\"Hello, World!\")"),
    ("haskell", "hs", "main :: IO ()\nmain = putStrLn \"Hello, World!\""),
    ("erlang", "erl", "-module(hello).\n-export([start/0]).\nstart() ->\n    io:format(\"Hello, World!~n\")."),
    ("elixir", "ex", "IO.puts \"Hello, World!\""),
    
    # System and assembly languages
    ("assembly_x86", "asm", "section .data\n    hello db 'Hello, World!',0\nsection .text\n    global _start\n_start:\n    mov eax, 4\n    mov ebx, 1\n    mov ecx, hello\n    mov edx, 13\n    int 0x80\n    mov eax, 1\n    int 0x80"),
    ("fortran", "f90", "program hello\n    print *, 'Hello, World!'\nend program hello"),
    ("cobol", "cob", "IDENTIFICATION DIVISION.\nPROGRAM-ID. HELLO-WORLD.\nPROCEDURE DIVISION.\nDISPLAY 'Hello, World!'.\nSTOP RUN."),
    ("pascal", "pas", "program HelloWorld;\nbegin\n    writeln('Hello, World!');\nend."),
    ("ada", "adb", "with Text_IO;\nprocedure Hello is\nbegin\n    Text_IO.Put_Line(\"Hello, World!\");\nend Hello;"),
    
    # Functional languages
    ("lisp", "lisp", "(format t \"Hello, World!~%\")"),
    ("scheme", "scm", "(display \"Hello, World!\")\n(newline)"),
    ("clojure", "clj", "(println \"Hello, World!\")"),
    ("f#", "fs", "printfn \"Hello, World!\""),
    ("ocaml", "ml", "print_endline \"Hello, World!\";;"),
    
    # Web and scripting languages
    ("html", "html", "<!DOCTYPE html>\n<html>\n<body>\n<h1>Hello, World!</h1>\n</body>\n</html>"),
    ("css", "css", "body:before {\n    content: \"Hello, World!\";\n}"),
    ("bash", "sh", "#!/bin/bash\necho \"Hello, World!\""),
    ("powershell", "ps1", "Write-Host \"Hello, World!\""),
    ("batch", "bat", "@echo off\necho Hello, World!"),
    ("vbscript", "vbs", "WScript.Echo \"Hello, World!\""),
    
    # Database languages
    ("sql", "sql", "SELECT 'Hello, World!' AS message;"),
    ("plsql", "sql", "BEGIN\n    DBMS_OUTPUT.PUT_LINE('Hello, World!');\nEND;"),
    
    # Markup and configuration languages
    ("xml", "xml", "<?xml version=\"1.0\"?>\n<message>Hello, World!</message>"),
    ("json", "json", "{\n    \"message\": \"Hello, World!\"\n}"),
    ("yaml", "yml", "message: Hello, World!"),
    ("toml", "toml", "message = \"Hello, World!\""),
    
    # Domain-specific languages
    ("r", "r", "cat(\"Hello, World!\\n\")"),
    ("matlab", "m", "disp('Hello, World!');"),
    ("mathematica", "nb", "Print[\"Hello, World!\"]"),
    ("julia", "jl", "println(\"Hello, World!\")"),
    ("latex", "tex", "\\documentclass{article}\\begin{document}Hello, World!\\end{document}"),
    
    # Esoteric and specialized languages
    ("brainfuck", "bf", "++++++++++[>+++++++>++++++++++>+++<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+."),
    ("whitespace", "ws", "   \t  \t   \n   \t \t\t  \n   \t \t \t \n   \t \t \t\t\n   \t \t\t  \n   \t  \n   \t     \n\t\n  \t\n\n\n"),
    ("befunge", "bf", ">              v\nv  \"Hello, World!\"<\n>  :#,_@"),
    
    # More mainstream languages
    ("objective_c", "m", "#import <Foundation/Foundation.h>\nint main() {\n    NSLog(@\"Hello, World!\");\n    return 0;\n}"),
    ("d", "d", "import std.stdio;\nvoid main() {\n    writeln(\"Hello, World!\");\n}"),
    ("nim", "nim", "echo \"Hello, World!\""),
    ("crystal", "cr", "puts \"Hello, World!\""),
    ("zig", "zig", "const std = @import(\"std\");\npub fn main() void {\n    std.debug.print(\"Hello, World!\\n\", .{});\n}"),
    
    # Additional languages from research
    ("actionscript", "as", "trace(\"Hello, World!\");"),
    ("algol", "alg", "'BEGIN' 'COMMENT' Hello World; OUTPUT(4,'('Hello World!')') 'END'"),
    ("apl", "apl", "⎕←'Hello, World!'"),
    ("applescript", "scpt", "display dialog \"Hello, World!\""),
    ("arduino", "ino", "void setup() {\n    Serial.begin(9600);\n    Serial.println(\"Hello, World!\");\n}\nvoid loop() {}"),
    ("awk", "awk", "BEGIN { print \"Hello, World!\" }"),
    ("basic", "bas", "10 PRINT \"Hello, World!\"\n20 END"),
    ("bcpl", "bcpl", "GET \"libhdr\"\nLET start() = VALOF\n$( writes(\"Hello World*N\")\n   RESULTIS 0\n$)"),
    ("boo", "boo", "print \"Hello, World!\""),
    ("chapel", "chpl", "writeln(\"Hello, World!\");"),
    ("clean", "icl", "module hello\nimport StdEnv\nStart = \"Hello, World!\""),
    ("clips", "clp", "(printout t \"Hello, World!\" crlf)"),
    ("coffeescript", "coffee", "console.log \"Hello, World!\""),
    ("curl", "curl", "{curl 7.0 applet}\n{value \"Hello, World!\"}"),
    ("dylan", "dylan", "format-out(\"Hello, World!\\n\");"),
    ("eiffel", "e", "class HELLO_WORLD\ncreate make\nfeature make\n    do print(\"Hello, World!%N\") end\nend"),
    ("elm", "elm", "import Html exposing (text)\nmain = text \"Hello, World!\""),
    ("euphoria", "ex", "puts(1, \"Hello, World!\\n\")"),
    ("factor", "factor", "\"Hello, World!\" print"),
    ("falcon", "fal", "> \"Hello, World!\""),
    ("forth", "fs", ". \" Hello, World!\" CR"),
    ("gamemonkey", "gm", "print(\"Hello, World!\");"),
    ("groovy", "groovy", "println \"Hello, World!\""),
    ("hack", "hh", "<?hh\necho \"Hello, World!\";"),
    ("icon", "icn", "procedure main()\n    write(\"Hello, World!\")\nend"),
    ("idris", "idr", "main : IO ()\nmain = putStrLn \"Hello, World!\""),
    ("inform", "inf", "[ Main;\n    print \"Hello, World!\";\n];"),
    ("io", "io", "\"Hello, World!\" println"),
    ("j", "ijs", "echo 'Hello, World!'"),
    ("lolcode", "lol", "HAI 1.2\nVISIBLE \"Hello, World!\"\nKTHXBYE"),
    ("mercury", "m", ":- module hello.\n:- interface.\n:- import_module io.\n:- pred main(io::di, io::uo) is det.\n:- implementation.\nmain(!IO) :-\n    io.write_string(\"Hello, World!\\n\", !IO)."),
    ("modula2", "mod", "MODULE HelloWorld;\nFROM InOut IMPORT WriteString, WriteLn;\nBEGIN\n    WriteString('Hello, World!');\n    WriteLn\nEND HelloWorld."),
    ("oberon", "mod", "MODULE HelloWorld;\nIMPORT Out;\nBEGIN\n    Out.String(\"Hello, World!\"); Out.Ln\nEND HelloWorld."),
    ("oz", "oz", "functor\nimport\n   System Application\ndefine\n   {System.showInfo 'Hello, World!'}\n   {Application.exit 0}\nend"),
    ("pike", "pike", "int main() {\n    write(\"Hello, World!\\n\");\n    return 0;\n}"),
    ("prolog", "pro", ":- initialization(main).\nmain :- write('Hello, World!'), nl, halt."),
    ("purebasic", "pb", "OpenConsole()\nPrintN(\"Hello, World!\")\nInput()\nCloseConsole()"),
    ("q", "q", "\"Hello, World!\""),
    ("racket", "rkt", "#lang racket\n(displayln \"Hello, World!\")"),
    ("rebol", "r", "print \"Hello, World!\""),
    ("smalltalk", "st", "Transcript show: 'Hello, World!'."),
    ("sml", "sml", "print \"Hello, World!\\n\";"),
    ("tcl", "tcl", "puts \"Hello, World!\""),
    ("vala", "vala", "void main() {\n    print(\"Hello, World!\\n\");\n}"),
    ("verilog", "v", "module hello;\n    initial begin\n        $display(\"Hello, World!\");\n        $finish;\n    end\nendmodule"),
    ("vhdl", "vhdl", "entity hello is\nend hello;\narchitecture behavior of hello is\nbegin\n    process\n    begin\n        report \"Hello, World!\";\n        wait;\n    end process;\nend behavior;"),
    ("visual_basic", "vb", "Module HelloWorld\n    Sub Main()\n        Console.WriteLine(\"Hello, World!\")\n    End Sub\nEnd Module"),
    
    # Additional specialized languages
    ("xslt", "xsl", "<?xml version=\"1.0\"?>\n<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n<xsl:template match=\"/\">\n<html><body>Hello, World!</body></html>\n</xsl:template>\n</xsl:stylesheet>"),
    ("xpath", "xpath", "\"Hello, World!\""),
    ("postscript", "ps", "%!PS-Adobe-2.0\n/Courier findfont 12 scalefont setfont\n100 700 moveto\n(Hello, World!) show\nshowpage"),
    ("makefile", "mk", "hello:\n\t@echo \"Hello, World!\"")
]

print(f"Total languages collected: {len(hello_world_programs)}")
print("First 10 languages:")
for i, (name, ext, code) in enumerate(hello_world_programs[:10]):
    print(f"{i+1}. {name} (.{ext})")
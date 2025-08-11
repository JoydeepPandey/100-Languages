; Hello World program in ASSEMBLY_X86
; Language: assembly_x86
; File extension: .asm

section .data
    hello db 'Hello, World!',0
section .text
    global _start
_start:
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, 13
    int 0x80
    mov eax, 1
    int 0x80
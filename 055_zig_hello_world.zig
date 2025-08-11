# Hello World program in ZIG
# Language: zig
# File extension: .zig

const std = @import("std");
pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}
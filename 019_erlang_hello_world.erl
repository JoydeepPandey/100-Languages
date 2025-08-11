% Hello World program in ERLANG
% Language: erlang
% File extension: .erl

-module(hello).
-export([start/0]).
start() ->
    io:format("Hello, World!~n").
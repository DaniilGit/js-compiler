#!/bin/bash

cd src/grammar

antlr4 -Dlanguage=Python3 JSLexer.g4

mkdir antlr-runtime-python
pip3 install --target "./antlr-runtime-python" antlr4-python3-runtime

mkdir build-antlr-lexer
mv JSLexer.interp ./build-antlr-lexer
mv JSLexer.py ./build-antlr-lexer
mv JSLexer.tokens ./build-antlr-lexer

cd build-antlr-lexer
touch __init__.py
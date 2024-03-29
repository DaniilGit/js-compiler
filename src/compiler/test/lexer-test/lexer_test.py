import sys
import pytest
sys.path.append('src/compiler')
from dump_tokens import dump_tokens
from antlr4 import *

test_paths = [
  ("example/example1.js", "src/compiler/test/lexer-test/right-test1.txt"),
  ("example/example2.js", "src/compiler/test/lexer-test/right-test2.txt"),
  ("example/example3.js", "src/compiler/test/lexer-test/right-test3.txt")
]
output = "src/compiler/test/lexer-test/output.txt"

@pytest.mark.parametrize("input,expected", test_paths)
def test_lexer(input, expected):
  output_stream = open(output, 'w')
  dump_tokens(input, output_stream)
  output_stream.close()

  assert ([row for row in open(output)] == [row for row in open(expected)])
#!/usr/bin/env python3
import pprint
import sys

import yaml

class BinaryConstructor(yaml.constructor.SafeConstructor):
    pass

BinaryConstructor.yaml_constructors = {
    key: val for key, val
              in BinaryConstructor.yaml_constructors.items()
              if key == 'tag:yaml.org,2002:binary'
}

class BinaryLoader(
        yaml.reader.Reader,
        yaml.scanner.Scanner,
        yaml.parser.Parser,
        yaml.composer.Composer,
        BinaryConstructor,
        # We use the base resolver to prevent implicit tagging.
        yaml.resolver.BaseResolver
    ):
    def __init__(self, stream):
        yaml.reader.Reader.__init__(self, stream)
        yaml.scanner.Scanner.__init__(self)
        yaml.parser.Parser.__init__(self)
        yaml.composer.Composer.__init__(self)
        BinaryConstructor.__init__(self)
        yaml.resolver.Resolver.__init__(self)

def load_archive(stream):
    return yaml.load(stream, Loader=BinaryLoader)

def main():
    f = sys.argv[1]
    with open(f) as h:
        parsed = load_archive(h)
        pprint.pprint(parsed)

if __name__ == '__main__':
    main()


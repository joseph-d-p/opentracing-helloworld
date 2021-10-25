import opentracing
import sys

tracer = opentracing.tracer


def say_hello(hello_to):
    span = tracer.start_span('say-hello')
    hello_str = 'Hello, %s!' % hello_to
    print(hello_str)
    span.finish()


assert len(sys.argv) == 2

hello_to = sys.argv[1]
say_hello(hello_to)

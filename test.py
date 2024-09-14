from midterms.ringbuffer import *

buf = RingBuffer(20)
buf.enqueue(20923)
x = buf.dequeue()
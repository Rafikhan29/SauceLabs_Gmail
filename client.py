import zerorpc

c = zerorpc.Client()
c.connect("tcp://54.255.189.247:4242")
print c.hello("Test RPC")

import zerorpc

c = zerorpc.Client()
c.connect("tcp://54.255.189.247:80")
print c.hello("Test RPC")

import binascii
import time

start=time.clock()
crcs=set([0xBA55CCDE,0xD1B824AF,0x07C3655E,0x4A4B71F7])
_tmp=set()
for i in xrange(97,126):
    for j in xrange(97,126):
	    for k in xrange(97,126):
		    for n in xrange(97,126):
			    str1=chr(i)+chr(j)+chr(k)+chr(n)
				#print hex(binascii.crc32(str1))
			    if binascii.crc32(str1)&0xffffffff in crcs:
				    print "crc32 of %s is -> %s" %(str1,hex(binascii.crc32(str1)&0xffffffff))
end=time.clock()
print "Used time: %f s" % (end - start)

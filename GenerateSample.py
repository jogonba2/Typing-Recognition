#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32api
import win32con
import sys
import time
import pickle

def _clear(): 
    for i in xrange(30): print "\n"

def _nErrors(a,b,B,I,S):
	V = {}
	V[0,0] = 0
	for i in xrange(1,len(b)+1): V[0,i] = i
	for i in xrange(1,len(a)+1): V[i,0] = i
	for i in xrange(1,len(a)+1):
		for j in xrange(1,len(b)+1):
			V[i,j] = min(V[i-1,j]+B(a,i-1),V[i,j-1]+I(b,j-1),V[i-1,j-1]+S(a,i-1,b,j-1))
	return V[len(a),len(b)]

def _generateSample():
    _clear()
    print u"Teclea: El veloz 1 murcielago hindu 2 comia feliz cardillo 3 y kiwi 5. La cigueña tocaba el 6 saxofon 1 detras del palenque 9 de paja. - Escrutinio 1337"
    m,sentence,times,l,replace,it,et,p       = 0,[],[],0,{190:46,188:44,189:45,192:241},0,0,0
    gs = u"El veloz 1 murcielago hindu 2 comia feliz cardillo 3 y kiwi 5. La cigueña tocaba el 6 saxofon 1 detras del palenque 9 de paja. - Escrutinio 1337"
    es = ""
    ls = len(gs)
    while True and l!=ls:
	for i in xrange(256):
	    k = win32api.GetAsyncKeyState(i)
	    if k==-32767:
		if i==16 or i==160: m=1
		elif i>=65 and i<=90:
		    if m==1: sentence.append(unichr(i))
		    else:    sentence.append(unichr(i+32))
		    et = time.clock()
		    times.append(et-it)
		    m,l,it = 0,l+1,et
		else: 
		    if i==8 and len(sentence)>0 and len(times)>0: sentence = sentence[:-1] ; l = max(l-1,0) ; times = times[:-1]
		    else: 
			if i!=1 and i!=13: 
			    sentence.append(unichr(i) if i not in replace else unichr(replace[i]))
			    et = time.clock()
			    times.append(et-it)
			    l,it = l+1,et
		_clear()
		print gs
		sys.stdout.write("".join(sentence))
		sys.stdout.flush()
    es = "".join(sentence)
    nErrors = _nErrors(gs,es,lambda x,i:1,lambda x,i:1,lambda x,i,y,j: 0 if x[i]==y[j] else 1)
    v = times+[nErrors]
    return v
    
if __name__ == "__main__":
    if len(sys.argv)>1:
	v = _generateSample()
	with open(sys.argv[1],"wb") as fd: pickle.dump(v,fd)
    else: print "Especifica el nombre del fichero para almacenar el patron"

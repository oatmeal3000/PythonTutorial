from time import time 


t = time()
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
total=[] 
for i in range (1000000): 
    a = [w for w in list]
    total.extend(a)
print "total run time:"
print time()-t

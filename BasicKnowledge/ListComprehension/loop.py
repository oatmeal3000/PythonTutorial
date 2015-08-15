from time import time 


t = time()
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 
total=[] 
for i in range (1000000): 
    for w in list: 
        total.append(w) 
print "total run time:"
print time()-t

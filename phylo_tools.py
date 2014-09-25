#!/usr/bin/env python

#this will be a module with my phylogenetic analysis tools. e.g. fasttree tree building, clustalo.

#assumed I have clustalo, fastteemp installed.
#first function will be to run clustalo from python.





#Run fasttreeMP outputs newick file.
def ClustalO(file_main_name):
    from subprocess import Popen, PIPE
    print 'Begin clustalo'
    clustalo = Popen(['time', 'clustalo', '-i', '%s' %(file_main_name), '-o', '%s_aligned_clustalo.fa' %(file_main_name), '--force'])
    clustalo.communicate()
    
    print 'Done with clustalo'


#want to run in the background but have an issue piping when nohup
def  FastTreeMP(file_main_name):
    from subprocess import Popen, PIPE
    import sys
    print "Begin FastTreeMP"
    FastTreeMP = Popen(['FastTreeMP', '-quiet', '-nopr', '-log', '%s_fasttree.log' %(file_main_name), '%s_aligned_clustalo.fa' %(file_main_name)],stdout=PIPE,shell=False)
    newick_out = open("%s_clustalo_fasttree.newick" %(file_main_name), 'w')
    newick_out.write(FastTreeMP.stdout.read())

    FastTreeMP.communicate()
    newick_out.close()
    print "Done with FastTreeMP"

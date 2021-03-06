#!/usr/bin/env python

#this will be a module with my phylogenetic analysis tools. e.g. fasttree tree building, clustalo.

#assumed I have clustalo, fastteemp installed.
#first function will be to run clustalo from python.





#Run fasttreeMP outputs newick file.
def ClustalO(file_main_name):
    from subprocess import Popen, PIPE
    print 'Begin clustalo'
    clustalo = Popen(['time', 'clustalo', '-i', '%s.fasta' %(file_main_name), '-o', '%s_clustalo.fasta' %(file_main_name), '--force', '--threads=4'])
    clustalo.communicate()
    
    print 'Done with clustalo'


#want to run in the background but have an issue piping when nohup
def  FastTreeMP(file_main_name):
    from subprocess import Popen, PIPE
    import sys
    print "Begin FastTreeMP"
    FastTreeMP = Popen(['FastTreeMP', '-quiet', '-nopr', '-log', '%s_fasttree.log' %(file_main_name), '%s.fasta' %(file_main_name)],stdout=PIPE,shell=False)
#phb is a newick file
    newick_out = open("%s.ph" %(file_main_name), 'w')
    newick_out.write(FastTreeMP.stdout.read())

    FastTreeMP.communicate()
    newick_out.close()
    print "Done with FastTreeMP"

#convert aligned fasta file and newick file to cdt file for visualization in treeview.

def fasta2cdt(file_main_name):
    from subprocess import Popen, PIPE
    import sys
    print 'Begin fasta and newick conversion to cdt'
    fasta2cdt = Popen(['fasta2cdt.py', file_main_name],stdout=PIPE, shell=False)
    print 'Done with conversion'


#input list of GIDs and output a dictionary with GID key and list value [species name,sequence]

def GID2seq(list_name_here):
    from subprocess import Popen, PIPE
    fasta_seqs = {}
    for GID in list_name_here:
        p = Popen(['blastdbcmd', '-db', 'nr', '-dbtype', 'prot', '-entry', GID, '-target_only','-outfmt', '%t\t%s'],stdout = PIPE)
        stdout = p.stdout.read()
        p.communicate()
        if stdout:
            stdout_split=stdout.split("\t")
            ID = stdout_split[0].strip()
            ID = ID.replace(' ', '_')  
            ID = ID.replace('[', '')
            ID = ID.replace(']', '')
            ID = ID.replace(',', '_')
            ID = ID.replace('/', '_')
            ID = ID.replace('__', '_')
            ID = ID.replace(':', '_')
            ID = ID.replace('.', '_')
            ID = ID.replace('(', '_')
            ID = ID.replace(')', '_')
            ID = ID.replace(';', '_')
            ID = ID.replace('+', '_')
            ID = ID.replace('=', '_')
            ID = ID.replace('__', '_')
            ID = ID.replace('__', '_')
            ID = ID.replace('__', '_')
       
            fasta_seqs[GID]=[ID,stdout_split[1]]
            #print stdout_split
        else:
            print "no GID sequecne %s" %(GID)

    return fasta_seqs

#build hmm within python.
#file has to have .fasta

def hmmbuild(file_main_name):
    from subprocess import Popen, PIPE
    hmmbuild = Popen(['hmmbuild', '--cpu', '4', '%s.hmm' %(file_main_name), '%s.fasta' %(file_main_name)])
    
    print 'Done with hmmbuild'

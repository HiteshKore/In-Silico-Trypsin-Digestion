'''
Author: Hitesh Kore
Institute: QIMR Berghofer Medical Research Institute, Brisbane, Australia
Email: Hitesh.Kore@qimrberghofer.edu.au
Description: This script performs in-silico trypsin digestion of the input protein sequences
and generates peptides between 7 to 35 amino acids.

'''
import re
import sys
import getopt
import os

class peptidecleaver():

    def __init__(self,input_file,output_file):
        fh=open(input_file,"r")
        head_seq={}
        fo=open(output_file,"w")

        fo.write("Header\tPeptides_count\tpeptides\n")
        for j in fh:
            matched_index=[]
            peptides=""
            string=""
            v=j.strip().split("\t")[1]
            head=j.strip().split("\t")[0]
            matched_index.append(0)

            for i in range(len(v) - 1):
                if v[i] == "K" and v[i + 1] != "P":


                    matched_index.append(i)
                elif v[i] == "R" and v[i + 1] != "P":

                    matched_index.append(i)
            matched_index.append(len(v))



            for j in range(0,len(matched_index)-1):
                if len(v[matched_index[j]:matched_index[j+1]])>=7 and len(v[matched_index[j]:matched_index[j+1]])<=35:
                    if j==0:
                        string=string+v[matched_index[j]:matched_index[j+1]+1]+","
                    else:
                        string = string + v[matched_index[j]+1:matched_index[j + 1] + 1] + ","

            if string=="":
                fo.write(head+"\t"+"0"+"\t"+"-\t"+v+"\n")
            else:
                temp=[]
                for s in re.split(",",string.strip()[:-1]):
                    if len(s) >= 7 and len(s) <= 35:
                        temp.append(s)
                fo.write(head+"\t"+str(len(temp))+"\t"+",".join(temp)+"\t"+v+"\n")


            matched_index=[]
            string=""

if __name__=="__main__":
    ############### Command-line arguments ################
    if len(sys.argv[1:]) <= 1:  #Indicates Incorrect arguments
        
        print( '''
        Incorrect arguments provided
        Command usage:python3 Insilico_Trypsin_digestion.py -i <input file> -o <output>    
         ''')
        sys.exit()
    else:
        options, args = getopt.getopt(sys.argv[1:],'i:o:')
        fg=False
        for opt, arg in options:
            if opt == '-i':
                if os.path.isfile(arg):
                    input_file = arg
                    fg=True
                else:
                    print("File does not exist")
                    sys.exit()   
            elif opt == '-o':    
                output_file = arg   
            else:
                print("Incorrect arguments provided")
                sys.exit()
        if fg==True:
            peptidecleaver(input_file,output_file)
import argparse
import functools
from multiprocessing import Pool
from Bio import SeqIO, bgzf
from Bio.Seq import Seq
from .util import fastq_chunk_interval, fastq_contain_barcode
import os

def barcode(input = None, output = None, output2 = None, contain = None, error = 1, rc_barcode = False, nproc = 1):
    """barcode subcommand
    Paramters
    ---------

    input : str
        output file name, auto detects .gz
    output : str
        output file name, auto detects .gz, contains fastq that contains specified barcode via contain
    contain: str
        barcode to detect, if multiple barcode, separate with comma: "AATTCCC,AGGGCCC,CCGGCG"
        # optional for "contain" sub-command:
        error: int
            allowed nucleotide mismatches (can be INDELs) when aligning, default to 1. 
        nproc: int
            number of parallel jobs, default to 1.
        rc_barcode: bool
            take reverse complement of the barcode when aligning, default to False.

    """

    args = list(locals().keys())

    local = locals()
    if all(bool(local[key]) is not True for key in args): 
        print("scutls fastq: warning: use 'scutls contain -h' for usage")
    # use True since args can be either None or False
    # arguments.py defines requirments of each argument

    # check if input fastq contains specified barcode:
    if contain:
        # prepare search pattern
        if not "," in contain:
            if rc_barcode:
                contain = str(Seq(contain).reverse_complement())
            barcode_pattern = "(" + contain + "){e<=" + str(error) + "}"
        else:
            barcode_pattern = ""
            barcodes = contain.split(",")
            for barcode in barcodes:
                if rc_barcode:
                    contain = str(Seq(contain).reverse_complement())
                barcode_pattern += "(" + barcode + "){e<=" + str(error) + "}(.*?)"
    
        # multiprocessing
        print("Saving to " + output + " ...")
        intervals = fastq_chunk_interval(input, nproc = nproc)
        p = Pool(nproc)
        res = p.map_async(
            functools.partial(
                fastq_contain_barcode,
                fastq = input,
                barcode_pattern = barcode_pattern),
                intervals.values()).get()
        fastq_hit, fastq_non_hit = [], []
        
        for x in range(len(res)):
            fastq_hit = fastq_hit + [hit for hit in res[x][0]]
            fastq_non_hit = fastq_non_hit + [non_hit for non_hit in res[x][1]]

        if not os.path.dirname(output) == "":
            os.makedirs(os.path.dirname(output), exist_ok=True)
        if output.endswith(".gz"):
            with bgzf.BgzfWriter(output, "wb") as outgz:
                SeqIO.write(sequences = fastq_hit, handle = outgz, format="fastq")
        else:
            SeqIO.write(fastq_hit, output, "fastq")
        
        if not output2 == None:
            print("Saving to " + output2 + " ...")
            if not os.path.dirname(output2) == "":
                os.makedirs(os.path.dirname(output2), exist_ok=True)
            if output2.endswith(".gz"):
                with bgzf.BgzfWriter(output2, "wb") as outgz:
                    SeqIO.write(sequences = fastq_non_hit, handle = outgz, format="fastq")
            else:
                SeqIO.write(fastq_non_hit, output2, "fastq")
        
        print("Done!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  '-i', type   = str)
    parser.add_argument('--output', '-o', type   = str)
    parser.add_argument('--output2', '-o2', type = str)
    parser.add_argument('--contain', '-c', action = str)
    parser.add_argument('--error',   '-e', type   = int)
    parser.add_argument('--rc_barcode', '-rcb', default = False)
    parser.add_argument('--num_processor', '-nproc', default = 1)
    
if __name__ == "__main__":
    main()

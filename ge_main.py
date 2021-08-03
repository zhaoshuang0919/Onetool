# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:56:49 2021

@author: zhi
"""
wasai

import os
from argparse import ArgumentParser
from generate_word import ge_word
from generate_english import ge_english

def build_parser():
    parser = ArgumentParser()
    
    help_out = 'destination (dir or file) of transformed file or files'
    parser.add_argument('--out-path', type=str,
                        dest='out_path', help=help_out, metavar='OUT_PATH',
                        required=True)
    
    parser.add_argument('--te', type=str,
                        dest='te',help='text style transfrom',
                        metavar='TE', required=True)

    parser.add_argument('--fg', type=int,
                        dest='fg',help='batch size for feedforwarding',
                        metavar='FG', required=True)

    return parser


def exists(p, msg):
    assert os.path.exists(p), msg


def check_opts(opts):
    exists(opts.out_path, 'Out path not found!')
    
    length = len(opts.te)
    if length<3 or length>12:
        print("Please enter a string of 3 to 12 characters in length")
        exit()
    if opts.fg != 0 and opts.fg !=1:
        print("Please enter flag 1 or 0")
        exit()
    #exists(opts.te, 'Text not found!')
    #exists(opts.fg, 'Flag not found!')


def main():
    parser = build_parser()
    opts = parser.parse_args()
    check_opts(opts)
    
    #te = "哈士奇小绘"
    #te = "hello world"
    #fg = 1
    
    out = opts.out_path
    te1 = opts.te
    fg1 = opts.fg
    
    #如果是英文返回True,中文返回false
    if te1[0].encode('UTF-8').isalpha():
        ge_english(out,te1,fg1)
    else:
        ge_word(out,te1,fg1)



if __name__ == '__main__':
    main()

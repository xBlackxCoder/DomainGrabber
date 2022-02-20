#!/usr/bin/python
# -*- coding: utf-8 -*-
#Recoding Doesn't Make You Programmer :)
#============== Moudles ===============#
import os
import time
import json
import threading
from time import sleep
from threading import Timer
#Install Requirements
try:
    import colorama
    import requests
    import termcolor
    from termcolor import colored
except:
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install termcolor')
#============== Moudles ===============#
colorama.init()
def ascii():
    """Prints the ascii logo"""
    print(colored("""
         ******    **                   **            
        /*////**  /**                  /**            
 **   **/*   /**  /**  ******    ***** /**  ** **   **
//** ** /******   /** //////**  **///**/** ** //** ** 
 //***  /*//// ** /**  ******* /**  // /****   //***  
  **/** /*    /** /** **////** /**   **/**/**   **/** 
 ** //**/*******  ***//********//***** /**//** ** //**
//   // ///////  ///  ////////  /////  //  // //   // 

By xBlacKx | @xBlackx_Coder | Channel:- @xBlackxCoder""",color = 'magenta'))

def Scarper():
    url = "https://urlscan.io/json/live/"

    resp = requests.get(url).json()

    for x in range(15):
        domains = resp["results"][x]["task"]["domain"]
        #add anything you need To avoid from results here as your wish :)
        if domains in ("t.me", "github.com", 'google.com', 'facebook.com', 'storage.googleapis.com', 'www.spotify.com'):
            pass
        else:
            file1 = open("Urlscan_Domains.txt", "a+")
            file1.writelines(f'{domains}\n')
            file1.close()
        print(colored(f"[+] Found Domain: {domains}",color = 'green'))
    sleep(10)
    Timer(1, Scarper()).start

def main():
    ascii()
    sleep(0.5)
    print(colored(f"Starting The Program Please Wait...",color = 'red'))
    Scarper()

if __name__ == '__main__':
    main()
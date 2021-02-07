#!/usr/bin/env python3


class Transaction:
    def __init__(self, sign):
        self.__sign = sign 
    
    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign):
        self.__sign = sign

class Block:
    def __init__(self):
        pass


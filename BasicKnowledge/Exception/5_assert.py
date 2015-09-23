#!/usr/bin/env python
# coding=utf-8

class Account(object):
    def __init__(self, number):
        self.balance = number 
        print "current balance ",self.balance

    def deposit(self, amount):
        assert amount > 0
        self.balance += amount 
        print "current balance ",self.balance

    def withdraw(self, amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
            print "current balance ",self.balance
        else:
            print "balance is not enough."

if __name__ == "__main__":
    a = Account(1000)
    a.deposit(100)
    a.withdraw(200)
    a.deposit(-10)

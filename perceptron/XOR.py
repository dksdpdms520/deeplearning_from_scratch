import numpy as np

def XOR(x1, x2):             #XOR 게이트: 배타적 논리합, 비선형, 다층 퍼셉트론
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
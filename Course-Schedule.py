{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\
        if len ( prerequisites ) == 0 : return True\
        checklist = [0] * numCourses\
        \
        for a, b in prerequisites :\
            key = b\
            flag = False\
            for c, d in prerequisites :\
                if prerequisites [ c-1 ] [ 0 ] == key :\
                    key = d\
                    flag = True\
            if flag == False : \
                checklist [ b ] = 1\
                checklist [ a ] = 1\
            \
        if checklist == [1] * numCourses : return True\
        return False}
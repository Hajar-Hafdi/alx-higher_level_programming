#!/usr/bin/python3
"""Outlines Pascal's Triangle function"""

def pascal_triangle(n):
    """depicts Pascal's Triangle of size n

    Returns list of lists of integers depicting the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for u in range(len(tri) - 1):
            tmp.append(tri[u] + tri[u + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

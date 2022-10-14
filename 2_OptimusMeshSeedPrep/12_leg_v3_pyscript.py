    p = mdb.models['6leg_4split_triangle_MERGE_trim'].parts['P6_leg_4split_triangle_exp2']
    e = p.edges
    pickedEdges = e.getClosest (coordinates=(($PNT_0_1_XCOORD$, 0, $PNT_0_1_ZCOORD$), ($PNT_0_2_XCOORD$, 0, $PNT_0_2_ZCOORD$), ($PNT_0_3_XCOORD$, 0, $PNT_0_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_1_1_XCOORD$, 0, $PNT_1_1_ZCOORD$), ($PNT_1_2_XCOORD$, 0, $PNT_1_2_ZCOORD$), ($PNT_1_3_XCOORD$, 0, $PNT_1_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_2_1_XCOORD$, 0, $PNT_2_1_ZCOORD$), ($PNT_2_2_XCOORD$, 0, $PNT_2_2_ZCOORD$), ($PNT_2_3_XCOORD$, 0, $PNT_2_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_3_1_XCOORD$, 0, $PNT_3_1_ZCOORD$), ($PNT_3_2_XCOORD$, 0, $PNT_3_2_ZCOORD$), ($PNT_3_3_XCOORD$, 0, $PNT_3_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_4_1_XCOORD$, 0, $PNT_4_1_ZCOORD$), ($PNT_4_2_XCOORD$, 0, $PNT_4_2_ZCOORD$), ($PNT_4_3_XCOORD$, 0, $PNT_4_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_5_1_XCOORD$, 0, $PNT_5_1_ZCOORD$), ($PNT_5_2_XCOORD$, 0, $PNT_5_2_ZCOORD$), ($PNT_5_3_XCOORD$, 0, $PNT_5_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_6_1_XCOORD$, 0, $PNT_6_1_ZCOORD$), ($PNT_6_2_XCOORD$, 0, $PNT_6_2_ZCOORD$), ($PNT_6_3_XCOORD$, 0, $PNT_6_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    pickedEdges = e.getClosest (coordinates=(($PNT_7_1_XCOORD$, 0, $PNT_7_1_ZCOORD$), ($PNT_7_2_XCOORD$, 0, $PNT_7_2_ZCOORD$), ($PNT_7_3_XCOORD$, 0, $PNT_7_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_0_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_0_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_0_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_0_1_XCOORD$ + 2*distToSym_1, 0, $PNT_0_1_ZCOORD$), ($PNT_0_2_XCOORD$ + 2*distToSym_2, 0, $PNT_0_2_ZCOORD$), ($PNT_0_3_XCOORD$ + 2*distToSym_3, 0, $PNT_0_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_1_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_1_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_1_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_1_1_XCOORD$ + 2*distToSym_1, 0, $PNT_1_1_ZCOORD$), ($PNT_1_2_XCOORD$ + 2*distToSym_2, 0, $PNT_1_2_ZCOORD$), ($PNT_1_3_XCOORD$ + 2*distToSym_3, 0, $PNT_1_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_2_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_2_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_2_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_2_1_XCOORD$ + 2*distToSym_1, 0, $PNT_2_1_ZCOORD$), ($PNT_2_2_XCOORD$ + 2*distToSym_2, 0, $PNT_2_2_ZCOORD$), ($PNT_2_3_XCOORD$ + 2*distToSym_3, 0, $PNT_2_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_3_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_3_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_3_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_3_1_XCOORD$ + 2*distToSym_1, 0, $PNT_3_1_ZCOORD$), ($PNT_3_2_XCOORD$ + 2*distToSym_2, 0, $PNT_3_2_ZCOORD$), ($PNT_3_3_XCOORD$ + 2*distToSym_3, 0, $PNT_3_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_4_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_4_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_4_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_4_1_XCOORD$ + 2*distToSym_1, 0, $PNT_4_1_ZCOORD$), ($PNT_4_2_XCOORD$ + 2*distToSym_2, 0, $PNT_4_2_ZCOORD$), ($PNT_4_3_XCOORD$ + 2*distToSym_3, 0, $PNT_4_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_5_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_5_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_5_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_5_1_XCOORD$ + 2*distToSym_1, 0, $PNT_5_1_ZCOORD$), ($PNT_5_2_XCOORD$ + 2*distToSym_2, 0, $PNT_5_2_ZCOORD$), ($PNT_5_3_XCOORD$ + 2*distToSym_3, 0, $PNT_5_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_6_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_6_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_6_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_6_1_XCOORD$ + 2*distToSym_1, 0, $PNT_6_1_ZCOORD$), ($PNT_6_2_XCOORD$ + 2*distToSym_2, 0, $PNT_6_2_ZCOORD$), ($PNT_6_3_XCOORD$ + 2*distToSym_3, 0, $PNT_6_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)
    distToSym_1 = $PNT_MID_1_XCOORD$ - $PNT_7_1_XCOORD$
    distToSym_2 = $PNT_MID_1_XCOORD$ - $PNT_7_2_XCOORD$
    distToSym_3 = $PNT_MID_1_XCOORD$ - $PNT_7_3_XCOORD$
    pickedEdges = e.getClosest (coordinates=(($PNT_7_1_XCOORD$ + 2*distToSym_1, 0, $PNT_7_1_ZCOORD$), ($PNT_7_2_XCOORD$ + 2*distToSym_2, 0, $PNT_7_2_ZCOORD$), ($PNT_7_3_XCOORD$ + 2*distToSym_3, 0, $PNT_7_3_ZCOORD$), ))
    edges_list = []
    for item in pickedEdges.values():
        edges_list.append(item[0])
    mytuple = tuple (edges_list)
    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)

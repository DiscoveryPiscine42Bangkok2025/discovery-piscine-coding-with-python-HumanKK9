def checkmate(board):
    i=0
    width=0
    boardarr=[]
    rowarr=[]
    Error=0
    for x in board:
        if x != '\n':
            rowarr.append(x)
        if width!=0 and i == width*width-1:
            boardarr.append(rowarr)
            rowarr=[]
        if width!=0 and i > width*width-1:
            print("Board unequal")
            Error=1
        if x == '\n':
            if width==0:
                width=i
            if i%width!=0:
                print("Board unequal")
                Error=1
                break
            boardarr.append(rowarr)
            rowarr=[]
            i-=1
        i+=1

    i=0
    Ki=-1
    Kj=-1
    for x in boardarr:
        j=0
        for y in boardarr[i]:
            if y=='K':
                if Ki!=-1:
                    print("More than one King")
                    Error=1
                    break
                Ki=i
                Kj=j
            if Error==1:
                break
            j+=1
        i+=1
    if Ki==-1:
        print("There is no King")
        Error=1
    #i is vertical, j is horizontal boardarr[i][j] is that
    
    #K King R rook P pawn Q queen B bishop, time to check the mate
    matechecked=0
    try:
        if boardarr[Ki+1][Kj+1] == "P" or boardarr[Ki+1][Kj-1] == "P":
            matechecked=1
    except:
        pass #out of bound, King at bottom
        
    def RookCheck(boardarr,Ki, Kj, i, j):
        n=0
        while True:
            n+=1
            try:
                square=boardarr[Ki+i*n][Kj+j*n]
                if square == "R" or square == "Q":
                    return 1 #checkmate
                elif square == "P" or square == "B":
                    return 0 #blocked, back
                else:
                    pass #empty: go on
            except: 
                return 0 #endboard, back
            
    def BishopCheck(boardarr,Ki, Kj, i, j):
        n=0
        while True:
            n+=1
            try:
                square=boardarr[Ki+i*n][Kj+j*n]
                if square == "B" or square == "Q":
                    return 1 #checkmate
                elif square == "P" or square == "R":
                    return 0 #blocked, back
                else:
                    pass #empty: go on
            except: 
                return 0 #endboard, back
            
    if RookCheck(boardarr,Ki, Kj, 1,0)==1:
        matechecked=1
    if RookCheck(boardarr,Ki, Kj, 0,1)==1:
        matechecked=1
    if RookCheck(boardarr,Ki, Kj, -1,0)==1:
        matechecked=1
    if RookCheck(boardarr,Ki, Kj, 0,-1)==1:
        matechecked=1

    if BishopCheck(boardarr,Ki, Kj, 1,1)==1:
        matechecked=1
    if BishopCheck(boardarr,Ki, Kj, -1,1)==1:
        matechecked=1
    if BishopCheck(boardarr,Ki, Kj, 1,-1)==1:
        matechecked=1
    if BishopCheck(boardarr,Ki, Kj, -1,-1)==1:
        matechecked=1



    if Error==1:
        pass
    elif matechecked==1:
        print("Success")
    else:
        print("Fail")


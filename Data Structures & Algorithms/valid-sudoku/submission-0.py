class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sum3=0
        arr1=[]
        arr2=[]
        arr3=[]
        flag = True
        k=0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board[i][j] = ""
                if (board[i][j] not in "123456789"):
                    flag= False
        for i in range(9):
            for j in range(9):
                if(board[i][j] != ""):
                     arr1.append(board[i][j])
                if(board[j][i] != ""):
                    arr2.append(board[j][i])
            if len(arr1) != len(set(arr1)):
                flag = False
            if len(arr2) != len(set(arr2)):
                flag = False
            arr1=[]
            arr2=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                low=j
                high=(j+3)
                k=j
                chk=[]
                while(k>=low and k<high):
                    if(board[i][k]!=""):
                        chk.append(board[i][k])
                    if(board[i+1][k]!=""):
                         chk.append(board[i+1][k])
                    if(board[i+2][k]!=""):
                         chk.append(board[i+2][k])
                    k+=1
                if (len(chk) != len(set(chk))):
                    flag = False
        return flag



        
        
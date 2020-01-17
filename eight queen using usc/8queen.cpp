#include<bits/stdc++.h>

using namespace std;

bool isSafe(vector<vector<int>>board, int row, int col) 
{ 
    int i, j; 
  
    
    for (i = 0; i < col; i++) 
        if (board[row][i]) 
            return false; 
  
    
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--) 
        if (board[i][j]) 
            return false; 
  
    
    for (i = row, j = col; j >= 0 && i < 8; i++, j--) 
        if (board[i][j]) 
            return false; 
  
    return true; 
} 

void printchess(vector<vector<int>>a)
{
    for(int i=0;i<8;i++)
    {
        for(int j=0;j<8;j++)
        {
            cout<<a[i][j]<<" | ";
        }
        cout<<endl;
    }
}

int checkNo(vector<vector<int>>v)
{
    int count=0;
    for(int i=0;i<8;i++)
    {
        for(int j=0;j<8;j++)
        {
            if(v[i][j]==1)
            count++;
        }
    }
    return count;
}

int checkcolumn(vector<vector<int>>v)
{
    int maxi=-1;
    for(int i=0;i<8;i++)
    {
        for(int j=0;j<8;j++)
        {
            if(v[i][j]==1)
            {
                maxi=max(j,maxi);
            }
        }
    }
    return maxi+1;
}


int main()
{
    vector<vector<int>>b(8, vector<int>(8, 0));
    queue<vector<vector<int>>>q;
    q.push(b);
    int count = 0;
    while(!q.empty())
    {
      vector<vector<int>> v;
      v=q.front();
      q.pop();
      int checkno = checkNo(v);
      if(checkno == 8)
      {
        count++ ;
        cout << count << "." << "\n" ;
        printchess(v);
        cout << endl;
      }
      else
      {
             int col = checkcolumn(v);
             for(int i=0;i<8;i++)
             {
               if(isSafe(v,i,col) == true)
               {
                   v[i][col] = 1;
                   q.push(v);
               }
               v[i][col]=0;
             }
             
      }
         

    
    }
 

    return 0;
}

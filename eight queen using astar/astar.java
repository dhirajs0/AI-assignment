import java.util.*;
	public class Assignment_2
	{
		int SIZE = 8;
		int opt_cost = SIZE;
		
		//some utility functions
		long factorial(int x)
		{
			long fact = 1;
			for(int i = 1;i<=x;i++)
				fact*=x;
			return fact;
		}
		
		long comb(int a, int b)
		{
			return factorial(a)/(factorial(b)*factorial(a-b));
		}
		
		//Creating initial state
		ChessBoard initialise()
		{
			String arr = "";
			for(int i=0;i<SIZE;i++)
				for(int j=0;j<SIZE;j++)
					arr+="0";
			return new ChessBoard(arr, 0, 0);
		}
		
		//Find the row where to insert the queen
		int find(String arr)
		{
		    int i;
			for(i=0;i<SIZE;i++)
			{
				int flag = 0;
				for(int j=0;j<SIZE;j++)
				{
					if(arr.charAt(SIZE*i+j) == '1')
					{
						flag = 1;
						break;
					}
				}
				if(flag == 0)
					return i;
			}
			return i;
		}
		
		//generate heuristic for current state
		long gen_heuristic(String arr)
		{
			long conf = 0;
			for(int i=0;i<SIZE;i++)
			{
				int sum_row = 0;
				int sum_col = 0;
				for(int j=0;j<SIZE;j++)
				{
					sum_row+=(int)arr.charAt(SIZE*i+j)-48;
					sum_col+=(int)arr.charAt(SIZE*j+i)-48;
				}
				conf+=comb(sum_row, 2) + comb(sum_col, 2);
			}
			for(int i=0;i<SIZE;i++)
			{
				int sum_left = 0;
				int sum_right = 0;
				for(int j=0;j+i<SIZE;j++)
				{
					sum_left+=(int)arr.charAt(SIZE*j+j+i)-48;
					sum_right+=(int)arr.charAt(SIZE*(j+i)+j)-48;
				}
				conf+=comb(sum_left, 2) + comb(sum_right, 2);
			}
			for(int i=0;i<2*SIZE-1;i++)
			{
				int sum_left = 0;
				int sum_right = 0;
				if(i<SIZE)
				{
				   for(int j=0;i-j>=0;j++)
				   {
					   sum_left+=(int)arr.charAt(SIZE*j+i-j)-48;
					   sum_right+=(int)arr.charAt(SIZE*(j+i)+j)-48;
		}
		conf+=comb(sum_left, 2) + comb(sum_right, 2);
		}
		for(int i=0;i<2*SIZE-1;i++)
		{
		int sum_left = 0;
		int sum_right = 0;
		if(i<SIZE)
		{
		for(int j=0;i-j>=0;j++)
		{
		sum_left+=(int)arr.charAt(SIZE*j+i-j)-48;
		}
		}
		else
		{
		for(int j=i-SIZE+1;j<SIZE;j++)
		{
		sum_right+=(int)arr.charAt(SIZE*j+i-j)-48;
		}
		}
		conf+=comb(sum_left, 2) + comb(sum_right, 2);
		}
		return conf;
		}
		
		//display valid state
		void display(String arr)
		{
		System.out.print(" ");
		for(int i=0;i<SIZE;i++)
		System.out.print("__ ");
		System.out.println();
		for(int i=0;i<SIZE;i++)
		{
		System.out.print("|");
		for(int j=0;j<SIZE;j++)
		{
		if(arr.charAt(SIZE*i+j)=='1')System.out.print("██|");
		else System.out.print("__|");
		}
		System.out.println();
		}
		}
		
		//driver function
		public static void main(String args[])
		{
		Assignment_2 obj = new Assignment_2();
		ChessBoard sol = obj.initialise();
		
		PriorityQueue<ChessBoard> ucs = new PriorityQueue<ChessBoard>(100, new BoardComparator());
		ucs.add(sol);
		
		int count = 1;
		
		System.out.println("//The black regions represent a queen at that place\n\n");
		
		while(!(ucs.isEmpty()))
		{
		//dequeue head of the queue
		ChessBoard chs = ucs.poll();
		String ans = chs.getBoard();
		
		//check if the current state is valid
		if(chs.getCost() + chs.getHeuristic() > obj.opt_cost)continue;
		
		//find where to insert the queen
		int i = obj.find(ans);
		
		//if the state is valid and solution is complete
		if(i==obj.SIZE)
		{
		System.out.println("========Solution "+count+"========");
		obj.display(ans);
		System.out.println("===========================\n");
		count++;
		}
		else
		{
		//explore the current node and enqueue it
		for(int j=0;j<obj.SIZE;j++)
		{
		ans = ans.substring(0, obj.SIZE*i+j)+"1"+ans.substring(obj.SIZE*i+j+1);
		ucs.offer(new ChessBoard(ans, chs.getCost()+1, obj.gen_heuristic(ans)));
		ans = chs.getBoard();
		}
		}	
		}
		}
	}
	
	class BoardComparator implements Comparator<ChessBoard>
	{
		public int compare(ChessBoard c1, ChessBoard c2) 
		{ 
	 if (c1.getCost() + c1.getHeuristic() > c2.getCost() + c2.getHeuristic())
	 return 1;
	 else if (c1.getCost() + c1.getHeuristic() < c2.getCost() + c2.getHeuristic()) 
	 return -1; 
	 return 0; 
	 } 
	}
	
	class ChessBoard
	{
		private String board;
		private int cost;
		private long heuristic;
	
		public ChessBoard(String board, int cost, long heuristic)
		{
			this.cost = cost;
		this.board = board;
		this.heuristic = heuristic;
		}
	
		int getCost()
		{
		return this.cost;
		}
		String getBoard()
		{
		return this.board;
		}
		long getHeuristic()
		{
		return this.heuristic;
		}
	
		void setCost(int cost)
		{
		this.cost = cost;
		}
		void setBoard(String board)
		{
		this.board = board;
		}
		void setHeuristic(long heuristic)
		{
		this.heuristic = heuristic;
		}
	}

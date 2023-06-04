# BlockChain

048888 – Project Check Point

Hannah & Dan Straussman 

Our chosen topic for the project is block propagation

  Week 4-5 – Read several papers, i.e: 
  
    1)	SimBlock: A Blockchain Network Simulator
    
    2)	Optimal Block Propagation and Incentive Mechanism for Blockchain Networks in 6G
    
    3)	https://www.sciencedirect.com/science/article/pii/S2096720921000439 (New paper)
    

  Week 6 – Open github repo for the project, choose which parameters we want to take in count and design the software structure (classes, libraries), define which are the graph results we will want to get from the simulations.
  
  We will do two main kinds of simulations: 
  
    1)	Propagation sequentially
    
    2)	Propagation parallelly
    
•	And we will exam which is preferred based on the block size/ network speed/ and so on

# Git repo:
  https://github.com/danstr1/BlockChain

# Topology: 
  Undirected graph G(V, E), where V is the set of vertices that represents nodes in the network and E is the set of edges that represent network connections between neighbors.
  
  Clusters? (Due to some papers, should be faster.)
  
# Difficulties: 

  differ between run time and simulation time
# Parameters:
  Block size
  
  Total number of nodes in the blockchain network
  
  Number of neighbor nodes (constant for all nodes)
  
  Network bandwidth
  
  Time to send a block (INV + GETDATA + Transaction)
  
  Time to receive a block (processing/validation)
  

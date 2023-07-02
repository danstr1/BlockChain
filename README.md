# BlockChain

048888 – Project Check Point

Hannah & Dan Straussman 

Our chosen topic for the project is block propagation

  Week 4-5 – Read several papers, i.e: 
  
    1)	SimBlock: A Blockchain Network Simulator
    
    2)	Optimal Block Propagation and Incentive Mechanism for Blockchain Networks in 6G
    
    3)	Security and performance evaluation of master node protocol based reputation blockchain in the bitcoin network
    

  Week 6 – Open github repo for the project, choose which parameters we want to take in count and design the software structure (classes, libraries), define which are the graph results we will want to get from the simulations.
  
  We will do two main kinds of simulations: 
  
    1)	Propagation sequentially
    
    2)	Propagation parallelly
    
•	And we will exam which is preferred based on the block size/ network speed/ and so on

# Git repo:
  https://github.com/danstr1/BlockChain

# Topology: 
  Undirected graph G(V, E), where V is the set of vertices that represents nodes in the network and E is the set of edges that represent network connections between neighbors.
  
The nodes are connected randomly to each other.

Clusters? (Due to some papers, should be faster.)
  
# Difficulties: 

•	Connecting randomly each node, cause that sometimes there are some nodes which can’t be connect while neighbors number remain constant. 

    o	Solved by connect the remains neighbors into themselves – TODO: check that don’t effect the propagation time
    
•	Differ between run time and simulation time

    o	We think that we’ll implement manually timer of units that we’ll count and define
  
# Parameters:
  Block size
  
  Total number of nodes in the blockchain network
  
  Number of neighbor nodes (constant for all nodes)
  
  Network bandwidth
  
  Time to send a block (INV + GETDATA + Transaction)
  
  Time to receive a block (processing/validation)
  
  ![image](https://github.com/danstr1/BlockChain/assets/24293665/ab74bbcb-6a4f-4cc4-b0b5-7bd786f7fa0a)

  
# Measurement: (still open to change)
•	Time to propagate block to whole network

•	Number of nodes get the block after X time units

•	Transaction propagation time VS Node with the highest transaction time out of X connect nodes

•	All the graphs will be comparing the serial and parallel block transaction

    o	There will be comparison with different parameters as well


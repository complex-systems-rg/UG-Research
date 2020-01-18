#include <agent.h>
#include <random>
#include <iostream>

class Simulation {
public:
	Simulation(int N, double defector_ratio, double gar, int t, int r, int p, int s, int _tau);
	void start();
	int getAvgC();
	int getAvgD();
    
private:
	void pairwise();
	void FisherYates(std::vector<int>& v, int beg, int end);
	void add_agents();
	bool wouldPlay(int i, int j);
	void deleteRandom(int i, std::set<int>& s);
	void deleteFromMemory(int i, int fg);
    
    int N;
	int D;
	int np;		//number of pairs
	double defector_ratio;
	std::vector<Agent*> agents;
	std::vector<std::pair<int, int> > pairs;
	int pc, pd;
	int avg_pc, avg_pd;
	int reward, sucker, temptation, punishment;
	int tau;
	double global_attention_ratio;
};

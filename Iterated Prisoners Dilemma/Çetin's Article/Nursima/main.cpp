/*
 * main.cpp
 *
 *  Created on: Sep 28, 2019
 *      Author: nursima
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <stdlib.h>
#include<set>
#include <iterator>

#define pb push_back
#define mp make_pair

using namespace std;

class Agent {
public:

	Agent(int N, bool c, int ac, int f) {
		cooperator = c;
		attention_capacity = ac;
		fs = f;
		coop_mem.resize(N);
		def_mem.resize(N);
	}
	Agent& operator=(const Agent& other) {

		cooperator = other.cooperator;
		attention_capacity = other.attention_capacity;
		coop_mem = other.coop_mem;
		def_mem = other.def_mem;
		fs = other.fs;
		return *this;
	}

	bool cooperator;
	unsigned int attention_capacity;
	vector<int> coop_mem, def_mem;
	set<int> knowns;
	int fs;		// FOD:0 FOC:1 FAR:2 FEQ:3 FMJ:4
};

class Simulation {
public:
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

	Simulation(int _N, double _defector_ratio, double _gar, int _t, int _r, int _p, int _s, int _tau) {
		//cout<<"Simulation constructor"<<endl;
		N = _N;
		defector_ratio = _defector_ratio;
		global_attention_ratio = _gar;
		D = N * defector_ratio;
		np = (N * N - N) / 2;
		pc = pd = avg_pc = avg_pd = 0;
		temptation = _t;
		reward = _r;
		punishment = _p;
		sucker = _s;
		tau = _tau;
	}

	void FisherYates(std::vector<int>& v, int beg, int end) {
		unsigned n = end - beg;
		if (n == 1)
			return;
		int r = rand() % (n - 1) + beg;
		int temp = v[beg];
		v[beg] = v[r];
		v[r] = temp;
		FisherYates(v, beg + 1, end);

	}

	void pairwise() {
		pairs.resize(np);
		std::vector<int> indices;
		for (int i = 0; i < np; i++) {
			indices.push_back(i);
		}
		FisherYates(indices, 0, np);

		int count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				pairs[indices[count]] = std::make_pair(i, j);
				count++;
			}
		}
	}
	void add_agents() {
		// if agent's memory capacity is homogeneous
		double ar = global_attention_ratio;

		int ac = N * ar;

		for (int i = 0; i < D; i++) {
			agents.push_back(new Agent(N, false, ac, 1));
		}
		for (int i = 0; i < N - D; i++) {
			agents.push_back(new Agent(N, true, ac, 1));
		}
	}
	bool wouldPlay(int i, int j) {
		return (agents[i]->coop_mem[j] >= agents[i]->def_mem[j])  && (agents[j]->coop_mem[i] >= agents[j]->def_mem[i]);
	}
	void deleteRandom(int i, set<int>& s) {
		unsigned index = rand() % s.size();
		int j = *s.find(index);

		agents[i]->coop_mem[j] = agents[i]->def_mem[j] = 0;

	}
	void deleteFromMemory(int i, int fg) {

		if (fg == 2) {
			deleteRandom(i, agents[i]->knowns);
			return;
		}
		if (fg == 4) {
			if (N - D == D)
				fg = 3;
			else
				fg = (N - D > D) ? 1 : 0;
		}
		if (fg == 3) {
			fg = rand() % 2;
		}

		set<int> to_be_deleted;

		for(int k : agents[i]->knowns) {

			if(!fg && agents[i]->coop_mem[k] < agents[i]->def_mem[k])
				to_be_deleted.insert(k);
			if(fg && agents[i]->coop_mem[k] > agents[i]->def_mem[k])
				to_be_deleted.insert(k);

		}
		deleteRandom(i, to_be_deleted);
	}

	void start() {

		add_agents();

		for (int p = 0; p < tau; p++) {
			pairwise();
			for (int i = 0; i < np; i++) {
				int a1 = pairs[i].first;
				int a2 = pairs[i].second;

				cout << a1 << " " << a2 << endl;

				if (wouldPlay(a1, a2)) {
					//cout<<"a1: "<<a1<<" a2: "<<a2<<endl;
					if (agents[a1]->cooperator && agents[a2]->cooperator) {
						pc += 2 * reward;
					} else if (!agents[a1]->cooperator && !agents[a2]->cooperator) {
						pd += 2 * punishment;
					} else {
						pc += sucker;
						pd += temptation;
					}

					if (agents[a1]->knowns.size() == agents[a1]->attention_capacity) {
						deleteFromMemory(a1, agents[a1]->fs);
					}
					if (agents[a2]->knowns.size() == agents[a2]->attention_capacity) {
						deleteFromMemory(a2, agents[a2]->fs);
					}
					if(agents[a2]->cooperator)
						agents[a1]->coop_mem[a2]++;
					else
						agents[a1]->def_mem[a2]++;

					agents[a1]->knowns.insert(a2);


					if (agents[a1]->cooperator)
						agents[a2]->coop_mem[a1]++;
					else
						agents[a2]->def_mem[a1]++;

					agents[a2]->knowns.insert(a1);

				}
				// else -> refusal -> zero gain
			}
		}

		avg_pc = pc / (N - D);
		avg_pd = pd / D;
	}
	int getAvgC() {
		return avg_pc;
	}
	int getAvgD() {
		return avg_pd;
	}
};

int main() {
	// perform the game <the specified realization number> times
	string name;
	//time_t t = time(NULL);
	srand(4);
	for (int i = 0; i < 10; i++) {
		// Simulation(int _N, double _defector_ratio, double global_attention_ratio, int _t, int _r, int _p, int _s, int _tau) {
		Simulation sim(50, 0.2, 0.3, 5, 3, 1, 0, 2);
		sim.start();
		name = "data1/" + to_string(i);
		ofstream fout(name);
		fout << sim.getAvgC() << "," << sim.getAvgD() << "," << sim.getAvgC() - sim.getAvgD() << endl;
		fout.close();
	}
	return 0;
}

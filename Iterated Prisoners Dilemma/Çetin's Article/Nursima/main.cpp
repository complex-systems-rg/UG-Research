#include <simulation.h>
#include <fstream>

using namespace std;

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

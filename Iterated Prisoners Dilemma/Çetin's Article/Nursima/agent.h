#include <vector>
#include <set>

class Agent {
public:

	Agent(int N, bool c, int ac, int f);
	Agent& operator=(const Agent& other);

	bool cooperator;
	unsigned int attention_capacity;
	std::vector<int> coop_mem, def_mem;
	std::set<int> knowns;
	int fs;		// FOD:0 FOC:1 FAR:2 FEQ:3 FMJ:4
};
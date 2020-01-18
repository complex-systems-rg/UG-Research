#include <agent.h>

Agent::Agent(int N, bool c, int ac, int f)
{
    cooperator = c;
    attention_capacity = ac;
    fs = f;
    coop_mem.resize(N);
    def_mem.resize(N);
}
Agent &Agent::operator=(const Agent &other)
{

    cooperator = other.cooperator;
    attention_capacity = other.attention_capacity;
    coop_mem = other.coop_mem;
    def_mem = other.def_mem;
    fs = other.fs;
    return *this;
}
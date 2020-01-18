#include <simulation.h>

Simulation::Simulation(int _N, double _defector_ratio, double _gar, int _t, int _r, int _p, int _s, int _tau)
{
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

void Simulation::FisherYates(std::vector<int> &v, int beg, int end)
{
    unsigned n = end - beg;
    if (n == 1)
        return;
    int r = std::rand() % (n - 1) + beg;
    int temp = v[beg];
    v[beg] = v[r];
    v[r] = temp;
    FisherYates(v, beg + 1, end);
}

void Simulation::pairwise()
{
    pairs.resize(np);
    std::vector<int> indices;
    for (int i = 0; i < np; i++)
    {
        indices.push_back(i);
    }
    FisherYates(indices, 0, np);

    int count = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            pairs[indices[count]] = std::make_pair(i, j);
            count++;
        }
    }
}
void Simulation::add_agents()
{
    // if agent's memory capacity is homogeneous
    double ar = global_attention_ratio;

    int ac = N * ar;

    for (int i = 0; i < D; i++)
    {
        agents.push_back(new Agent(N, false, ac, 1));
    }
    for (int i = 0; i < N - D; i++)
    {
        agents.push_back(new Agent(N, true, ac, 1));
    }
}
bool Simulation::wouldPlay(int i, int j)
{
    return (agents[i]->coop_mem[j] >= agents[i]->def_mem[j]) && (agents[j]->coop_mem[i] >= agents[j]->def_mem[i]);
}
void Simulation::deleteRandom(int i, std::set<int> &s)
{
    unsigned index = std::rand() % s.size();
    int j = *s.find(index);

    agents[i]->coop_mem[j] = agents[i]->def_mem[j] = 0;
}
void Simulation::deleteFromMemory(int i, int fg)
{

    if (fg == 2)
    {
        deleteRandom(i, agents[i]->knowns);
        return;
    }
    if (fg == 4)
    {
        if (N - D == D)
            fg = 3;
        else
            fg = (N - D > D) ? 1 : 0;
    }
    if (fg == 3)
    {
        fg = std::rand() % 2;
    }

    std::set<int> to_be_deleted;

    for (int k : agents[i]->knowns)
    {

        if (!fg && agents[i]->coop_mem[k] < agents[i]->def_mem[k])
            to_be_deleted.insert(k);
        if (fg && agents[i]->coop_mem[k] > agents[i]->def_mem[k])
            to_be_deleted.insert(k);
    }
    deleteRandom(i, to_be_deleted);
}

void Simulation::start()
{

    add_agents();

    for (int p = 0; p < tau; p++)
    {
        pairwise();
        for (int i = 0; i < np; i++)
        {
            int a1 = pairs[i].first;
            int a2 = pairs[i].second;

            //std::cout << a1 << " " << a2 << std::endl;

            if (wouldPlay(a1, a2))
            {
                //cout<<"a1: "<<a1<<" a2: "<<a2<<endl;
                if (agents[a1]->cooperator && agents[a2]->cooperator)
                {
                    pc += 2 * reward;
                }
                else if (!agents[a1]->cooperator && !agents[a2]->cooperator)
                {
                    pd += 2 * punishment;
                }
                else
                {
                    pc += sucker;
                    pd += temptation;
                }

                if (agents[a1]->knowns.size() == agents[a1]->attention_capacity)
                {
                    deleteFromMemory(a1, agents[a1]->fs);
                }
                if (agents[a2]->knowns.size() == agents[a2]->attention_capacity)
                {
                    deleteFromMemory(a2, agents[a2]->fs);
                }
                if (agents[a2]->cooperator)
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
int Simulation::getAvgC()
{
    return avg_pc;
}
int Simulation::getAvgD()
{
    return avg_pd;
}

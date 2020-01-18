all:	main.o simulation.o agent.o
	g++ -std=c++11 main.o simulation.o agent.o

main.o:	main.cpp simulation.h
	g++ -std=c++11 -c -I. main.cpp

simulation.o:	simulation.cpp simulation.h agent.h
	g++ -std=c++11 -c -I. simulation.cpp

agent.o:	agent.cpp agent.h
	g++ -std=c++11 -c -I. agent.cpp

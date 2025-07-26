#include <iostream>
#include "hello.h"
#include "init.h"

using namespace std;

int main(int argc, char* argv[]) {
	cout << "Hello Dungeon!" << endl;
	hello();
	init(argc, argv);
	return 0;
}
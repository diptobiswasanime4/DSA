#include <SDL3/SDL.h>
#include <iostream>

using namespace std;

int hello() {
	cout << "Hello World" << endl;

	SDL_Window* window;
	SDL_Renderer* renderer;

	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		cerr << "SDL failed to init" << SDL_GetError() << endl;
		return false;
	}

	window = SDL_CreateWindow("SDL Window", 800, 600, 0);
	if (!window) {
		cerr << "Window failed to init" << SDL_GetError() << endl;
		return false;
	}

	renderer = SDL_CreateRenderer(window, nullptr);
	if (!renderer) {
		cerr << "Renderer failed to init" << SDL_GetError() << endl;
		return false;
	}

	return 0;
}

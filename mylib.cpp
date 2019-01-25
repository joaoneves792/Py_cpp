#include <iostream>

extern "C"{
#include <stdarg.h>
#include "mylib.h"
}

void (*g_callback)(int, int, int* ) = nullptr;
int g_lst[] = {1, 2, 3};


void init(int a){
	std::cout << "Init: " << a << std::endl;
}

void addStuff(int a, int count, int* list){
	std::cout << "C++: Got " << a << " : ";
	for(int i = 0; i < count; i++){
		std::cout << list[i] << " ";
	}
	std::cout << std::endl;
}

void addStuffVariadic(int a, int count, ...){
	va_list list;
	va_start(list, count);
	std::cout << "C++: Got " << a << " : ";
	for(int i = 0; i < count; i++){
		std::cout << va_arg(list, int) << " ";
	}
	va_end(list);
	std::cout << std::endl;
}

void flush(){
	std::cout << "Flush!" << std::endl;
	if(g_callback)
		(*g_callback)(10000, 3, g_lst);
}


void registerCallback(void(*callback)(int a, int count, int* list)){
	g_callback = callback;
}

void shutdown(){
	std::cout << "Shutdown" << std::endl;
}

#ifndef __MYLIB_H__
#define __MYLIB_H__

void init(int a);
void addStuff(int a, int count, int* list);
void addStuffVariadic(int a, int count, ...);
void flush();
void registerCallback(void(*callback)(int a, int count, int* list));
void shutdown();

#endif //__MYLIB_H__

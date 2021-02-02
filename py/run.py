from jsrun.core import JSRUN

core = JSRUN(0, "")

code = ("""
#include <stdio.h>
int main()
{
   printf("Hello, World!");
   return 0;
}
""")

print(core.launch("c", code))
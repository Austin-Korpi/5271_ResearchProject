LIB_NAME=ffmalloc

LIB_SHARED_NPMT=lib${LIB_NAME}npmt.so

LIB_OBJS_NPMT=ffmallocnpmt.o


#CFLAGS=-Wall -Wextra -fPIC -c -g -O3
CFLAGS=-Wall -Wextra -Wno-unknown-pragmas -fPIC -c -g -O3 -DFF_GROWLARGEREALLOC -D_GNU_SOURCE
#CFLAGS=-Wall -Wextra -fPIC -c -O3 -DFF_PROFILE
CC=gcc

all: sharednpmt 

sharednpmt: ${LIB_SHARED_NPMT}

${LIB_SHARED_NPMT}: ${LIB_OBJS_NPMT}
	${CC} -o $@ -shared -fPIC -pthread $^


${LIB_OBJS_NPMT}: ffmalloc.c
	${CC} ${CFLAGS} ffmalloc.c -o $@


ffmalloc.c: ffmalloc.h

clean:
	rm *.o
	rm *.so

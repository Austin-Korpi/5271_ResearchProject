LIB_NAME=ffmalloc

LIB_SHARED_NPMT=lib${LIB_NAME}npmt.so
LIB_SHARED_NU=lib${LIB_NAME}nu.so

LIB_OBJS_NPMT=ffmallocnpmt.o
LIB_OBJS_NU=ffmallocnu.o


#CFLAGS=-Wall -Wextra -fPIC -c -g -O3
CFLAGS=-Wall -Wextra -Wno-unknown-pragmas -fPIC -c -g -O3 -DFF_GROWLARGEREALLOC -D_GNU_SOURCE
#CFLAGS=-Wall -Wextra -fPIC -c -O3 -DFF_PROFILE
CC=gcc

all: sharednpmt sharednu

sharednpmt: ${LIB_SHARED_NPMT}
sharednu: ${LIB_SHARED_NU}

${LIB_SHARED_NPMT}: ${LIB_OBJS_NPMT}
	${CC} -o $@ -shared -fPIC -pthread $^

${LIB_SHARED_NU}: ${LIB_OBJS_NU}
		${CC} -o $@ -shared -fPIC -pthread $^


${LIB_OBJS_NPMT}: ffmalloc.c
	${CC} ${CFLAGS} ffmalloc.c -o $@

${LIB_OBJS_NU}: ffmalloc.c
	${CC} ${CFLAGS} ffmalloc.c -DNEVER_UNMAP -o $@



ffmalloc.c: ffmalloc.h

clean:
	rm *.o
	rm *.so

# 5271 Group Project

The goal is to extend ffmalloc/hushvac to support mmap and munmap with the strong guarantee that memory will  never be reused/won't be reused while there are pointers to it. 

Most programs that use MAP_FIXED want to reuse memory. We allow this.

### Reference Sources
ffmalloc: https://github.com/bwickman97/ffmalloc

huscvac: https://github.com/cssl-unist/hushvac

## Installation and Use
Compile with `make all`

Replace libc memory allocation by preloading the library.

    LD_PRELOAD=/path/to/ffmallocnpmt.so /path/to/executable

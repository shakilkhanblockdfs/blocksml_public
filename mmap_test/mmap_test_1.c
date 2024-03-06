#include <stdio.h>
#include <sys/stat.h>

#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(){

int fd, rc , ii;
char *ptr;
struct stat st;
size_t size;

fd = open("hello1.raw", O_RDWR);

rc = fstat(fd, &st);
fprintf(stderr, "stat() = %d\n", rc);
size=st.st_size;
fprintf(stderr, "size=%zu\n", size);

ptr = mmap(0, size, PROT_READ|PROT_WRITE|PROT_EXEC ,MAP_SHARED , fd, 0);
fprintf(stderr, "address of hello1.raw: %p\n", ptr);

for (ii=0; ii < size/sizeof *ptr; ii++) {
   printf("data in raw[%d]: %c\n", ii, ptr[ii]);
        }

	ptr[ii-1] = 'Z';

rc = munmap(ptr, size);
fprintf(stderr, "unmap() = %d\n", rc);
close(fd);

return 0;
}

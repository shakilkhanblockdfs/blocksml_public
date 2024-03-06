
#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int main()
{
	char *dst;
	char *tmp;
	int fdout =  -1;
	struct stat st;
	size_t size;	

	if ((fdout = open ("./hello.txt", O_RDWR | O_CREAT, 0777)) < 0)//edited here
	{
		printf ("can't create %s for writing", "./hello.txt");
		return 0;
	}

	fstat(fdout, &st);
	size=st.st_size;

	printf("File size is %lu\n", size);

	if ((dst = (char *)mmap (0, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_SHARED, fdout, 0)) == (char *) -1)
	{
		printf ("mmap error for output");
		return 0;
	}

	printf("Address of the pointer received after mapping is %x\n", dst);

	tmp = dst;
	for(int i=0; i<size/sizeof(*dst);i++)
	{
		printf("%c ", dst[i]);
	}

	munmap(dst,size );	
	return 0;
}











#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

using namespace std;

// study the source code of the Nautilus and check how it works
// How does the dropbox detects the file changes and uploads only the diff
// Does the google drive also uploads the diff only or the entire file
// How does the VI or emac makes changes to the dirty buffer and write contents in between.


class skmmap{
private:
	char *ptr;
	off_t pos;
	int fd;
	mode_t mode;
	struct stat st;
	size_t fsize;
	int skerror;

	//Check if the size integer is correct or size can be something like off_t for large files
	//What is the size of the largest files.
	//todo:shakil... do with the file directory and path so that filename will have the path as well.
	char filename[256];
public:
	skmmap(const char *filename)
	{
		strncpy(this->filename, filename, sizeof(filename)-1);

		pos = 0;
		ptr = NULL;
		fd = -1;
		mode = 0777;
		st.st_size = 0;
		fsize = 0;
		skerror = 0;

		if ((fd = open (filename, O_RDWR | O_CREAT, mode)) < 0)//edited here
		{
			printf("Error in opening the file %s error=%s\n", filename, strerror(errno));
			skerror = -1;
		}
		fstat(fd, &st);   //todo:shakil..Check the return value of fstat
		fsize=st.st_size;
		printf("fsize=%lu\n", fsize);
		//todo:shakil....In future flags like PROT_READ and others can be passed as argument to constructor

		if ((ptr = (char *)mmap (0, fsize, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_SHARED, fd, 0)) == (char *) -1)
		{
			printf ("mmap error for output error=%s\n", strerror(errno));
			cleanup();
			skerror = -2;
		}
	}
	int read(size_t num, char *buffer);  ///The buffer of appropriate size(num) is provided by the caller.
	int write(off_t loc, size_t num, char *buffer, bool trunc); ///The buffer of appropriate size(num) is provided by the caller.
	int sklseek(off_t offset, int whence); 
	void cleanup();
};

void skmmap::cleanup()
{
	close(fd);
	ptr = NULL;
	fsize = st.st_size = 0;
	pos = 0;
}

int skmmap::read(size_t num, char *buffer)
{
	size_t i,j;
	if(fd == -1)
	{
		printf("Error in opening the file %s\n", filename);
		return -1;
	}

	printf("value of pos=%lu\n", pos);

	size_t max_num_bytes = fsize-pos;
	printf("max_num_bytes=%lu\n", max_num_bytes);
	size_t data_available  = num < max_num_bytes?num: max_num_bytes;
	printf("datavaailable=%lu\n", data_available);

	for(i=0, j= pos; i<data_available; ++i, ++j)
	{
		buffer[i] = ptr[j];
	}	

	pos += data_available; 
	sklseek(pos, SEEK_SET);	
	printf("------------------\n");
	return data_available;   
}


//loc is loc bytes from the start of the file
int skmmap::write(off_t loc, size_t num, char *buffer, bool trunc=false)
{
	printf("ole fsize=%lu\n", fsize);
	printf("loc=%lu\n", loc);
	printf("num=%lu\n", num);
	if(loc+num > fsize || trunc)
	{
		printf("Inside here\n");
		printf("new fsize=%lu\n", fsize);
		munmap(ptr, fsize);
		fsize = loc+num;
		if ((ptr = (char *)mmap (0, fsize, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_SHARED, fd, 0)) == (char *) -1)
		{
			printf ("mmap error for output error=%s\n", strerror(errno));
			cleanup();
			skerror = -3;
		}
	}

	for(size_t i=0, j=loc; i<num; ++j, ++i)
	{
		ptr[j] = buffer[i];
	}

	fsync(fd);
	fdatasync(fd);
	//munmap(ptr, fsize);

	//Please ensure that fszie or st.st_size is updated.
	return num;    ///todo:shakil...it will always be num except for when the filesize limit of fs is increased to size
}


int skmmap::sklseek(off_t offset, int whence)
{
	return lseek(fd, pos, SEEK_SET);	
}

int main()
{
	char buffer[100] = {0};
	skmmap obj1("./hello.txt");

	obj1.read(10, buffer);
	printf("%s\n", buffer);

	for(int i=0;i<10;i++)
		buffer[i] = 0;

	obj1.read(100, buffer);
	printf("%s\n", buffer);

	for(int i=0;i<100;i++)
		buffer[i] = 0;

	obj1.read(100, buffer);
	printf("%s\n", buffer);

	obj1.write(3,sizeof("FUCKersikinghello"),"FUCKersikinghello", true); //The last flasg is for truncate of the file to the (start_loc+num_bytes)

	for(int i=0;i<100;i++)
		buffer[i] = 0;

	obj1.read(100, buffer);
	printf("%s\n", buffer);
	return 0;

}
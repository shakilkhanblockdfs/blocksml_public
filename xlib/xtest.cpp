/*
Copyright (C) 2009-2017 Free Software Foundation, Inc.

Written by Shakil A Khan <shakilk1729@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street - Fifth Floor, Boston, MA 02110-1301, USA.
*/


#include <xstring.h>
#include <iostream>
#include <sstream>
#include <list>
#include <vector>
#include <xunistd.h>

using namespace std;


int main()
{
	vector <xstring> l2;
	list <xstring>	l1  {"hello","pello","zello"};
	for(auto l=l1.begin();l !=l1.end();++l)
		cout << *l<<endl;

	//xstring hi = "Hi there how are you.. vsfsd";
	xstring hi = "";
	xstring hii= " ";
	l2 = xsplit(hi);

	cout << " size of l2= " << l2.size()<<endl;

	for(auto l = l2.begin(); l !=l2.end(); ++l)
		cout << *l<<"<"<<">"<<endl;

	xstring myfile = "/tmp/shakil/hello" ;

	if(xaccess(myfile, F_OK) == 0)
	{	
		cout << "file ="<<myfile<< " exist" <<endl;
	}
	else
	{
		cout << "file ="<<myfile<< " doesn not exist" <<endl;
	}

	xstring ss = "this is in all Lower except Two";
	xtolower(ss);
	cout << ss<<endl;

	xtoupper(ss);
	cout << ss<<endl;
	
	xstring needle = "excep";
	cout << xstrcasestr(ss,needle)<<endl;

	ss = "this is in all Lower except Two";
	cout << xstrnstr(ss,needle,26)<<endl;
	
	xstring win_path = "c:\\program Files\\Validedge\\velab";
	vector<xstring> v = xsplit(win_path,"\\");

	cout <<"------------------------\n";
	for(auto vv = v.begin(); vv != v.end(); ++vv)
		cout << *vv<<endl;
		
	return 0;
}

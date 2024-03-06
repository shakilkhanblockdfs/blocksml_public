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


#include <iostream>
#include <string>

using namespace std;

string xstrstr(const string &haystack, const string &needle)
{
	size_t pos = haystack.find(needle);
	if (pos != std::string::npos)
		return haystack.substr(pos);
	return string("");
}

void xtoupper(string &s)
{
	std::transform(s.begin(),s.end(), s.begin(), ::toupper);
}

void xtolower(string &s)
{
	std::transform(s.begin(),s.end(), s.begin(), ::tolower);
}

string xstrcasestr(const string &haystack, const string &needle)
{
	string lhaystack(haystack);
	string lneedle(needle);

	xtolower(lhaystack);
	xtolower(lneedle);

	size_t pos = lhaystack.find(lneedle);
	if (pos != std::string::npos)
		return haystack.substr(pos);
	return string("");
}

int main()
{
	string s = "Hey there whats up. we ill try to search in this";
	string needle = "whats";

	cout << xstrstr(s, needle)<<endl;

	xtoupper(s);
	cout <<s<<endl;

	cout << xstrcasestr(s, needle)<<endl;
}
